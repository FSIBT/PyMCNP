import os
import sys
import datetime
import pathlib

import pytest

import pymcnp

from ..executables import fake_executable

FAKE = """import sys, pathlib
arguments = dict(argument.split('=', 1) for argument in sys.argv[1:])
text = pathlib.Path(arguments['inp']).read_text()
pathlib.Path(arguments['outp']).write_text('  fatal error.  surface 7 not found\\n' if 'FAIL' in text else 'ok\\n')
pathlib.Path(arguments['ptrac']).write_text('ptrac\\n')
pathlib.Path(arguments['runtpe']).write_text('runtpe\\n')
sys.exit(3 if 'EXIT' in text else 0)
"""


@pytest.fixture
def fake(tmp_path: pathlib.Path) -> str:
    path = tmp_path / 'bin' / 'fake-mcnp'
    path.parent.mkdir()
    return fake_executable(path, FAKE)


def _inps(inp: pymcnp.Inp, count: int, title: str = 'T') -> list[pymcnp.Inp]:
    inps = []
    for i in range(count):
        copy = pymcnp.Inp.from_mcnp(inp.to_mcnp())[0]
        copy.title = f'{title} {i}\n'
        inps.append(copy)
    return inps


class Test_Result:
    def test_ok(self, tmp_path: pathlib.Path) -> None:
        kwargs = {'index': 0, 'directory': tmp_path, 'inp': tmp_path / 'a.inp', 'outp': tmp_path / 'a.outp', 'ptrac': None, 'runtpe': None, 'log': tmp_path / 'a.log'}
        assert pymcnp.Result(returncode=0, **kwargs).ok
        assert not pymcnp.Result(returncode=1, **kwargs).ok
        assert not pymcnp.Result(returncode=0, fatal_errors=['x'], **kwargs).ok
        assert not pymcnp.Result(returncode=0, **{**kwargs, 'outp': None}).ok


class Test_Run:
    def test___post_init___invalid(self, inp: pymcnp.Inp) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run((inp,), '')
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run((inp,), 'echo', max_workers=0)
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run((inp,), 'echo', names=['a', 'b'])
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run((inp, inp), 'echo', names=['a', 'a'])
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run((inp,), 'echo', names=['../escape'])
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run((inp, inp), 'echo', names='same')

    def test_missing_command_is_named(self, inp: pymcnp.Inp) -> None:
        with pytest.raises(pymcnp.abc.Error, match='MCNP command not found: nosuchmcnp6') as error:
            pymcnp.Run((inp,), 'nosuchmcnp6')
        assert 'PATH' in error.value.body

    def test_hooks_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        run = pymcnp.Run((inp,), command='echo')
        run.prehook_file(tmp_path, 0)
        run.prehook_batch(tmp_path)
        run.posthook_batch(tmp_path)

    def test_run_returns_results(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        results = pymcnp.Run(_inps(inp, 3), command=fake).run(tmp_path / 'out')

        assert [result.index for result in results] == [0, 1, 2]
        for result in results:
            assert result.ok and result.returncode == 0 and result.fatal_errors == []
            assert result.inp.name == f'run-{result.index:05}.inp'
            assert result.outp and result.outp.read_text() == 'ok\n'
            assert result.ptrac and result.ptrac.name == f'run-{result.index:05}.ptrac'
            assert result.runtpe and result.log.exists()

    def test_run_names_template_and_sequence(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        results = pymcnp.Run(_inps(inp, 2), command=fake, names='case-{index}').run(tmp_path / 'a')
        assert [result.outp.name for result in results if result.outp] == ['case-0.outp', 'case-1.outp']

        results = pymcnp.Run(_inps(inp, 2), command=fake, names=['x', 'y']).run(tmp_path / 'b')
        assert [result.ptrac.name for result in results if result.ptrac] == ['x.ptrac', 'y.ptrac']

    def test_run_limits_workers(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        results = pymcnp.Run(_inps(inp, 4), command=fake, max_workers=1).run(tmp_path)
        assert len(results) == 4 and all(result.ok for result in results)

    def test_run_raises_on_failure_after_all_finished(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        inps = _inps(inp, 3)
        inps[1].title = 'FAIL\n'
        calls = []

        class Hooked(pymcnp.Run):
            def posthook_file(self, result):
                calls.append(result.index)

            def posthook_batch(self, path):
                calls.append('batch')  # pragma: no cover (must not run: a run failed, which the test asserts)

        with pytest.raises(pymcnp.abc.Error) as error:
            Hooked(inps, command=fake).run(tmp_path)

        assert 'run-00001' in str(error.value.body) and 'surface 7 not found' in str(error.value.body)
        assert sorted(calls) == [0, 2]  # the other runs finished, no batch hook
        assert len(list(next(tmp_path.glob('pymcnp-*')).glob('run-*'))) == 3

    def test_relative_command(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
        # A command given relative to the working directory, e.g., ``./mcnp6``, although each run starts in its own directory.
        monkeypatch.chdir(tmp_path)
        (result,) = pymcnp.Run(_inps(inp, 1), command=str(pathlib.Path('bin') / 'fake-mcnp')).run('out')
        assert result.ok

    def test_command_on_path(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
        # ``mcnp6`` is found on ``PATH``; on Windows also as ``mcnp6.exe``, ``mcnp6.bat`` or ``mcnp6.cmd``.
        monkeypatch.setenv('PATH', os.pathsep.join([str(pathlib.Path(fake).parent), os.environ['PATH']]))
        (result,) = pymcnp.Run(_inps(inp, 1), command='fake-mcnp').run(tmp_path)
        assert result.ok

    def test_run_exit_code_is_a_failure(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        inps = _inps(inp, 1, title='EXIT')
        with pytest.raises(pymcnp.abc.Error, match='Run failed'):
            pymcnp.Run(inps, command=fake).run(tmp_path)

    def test_missing_outp_is_named(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        # ``echo`` exits with 0 but writes no output file: say so, and ``check=False`` dry-runs.
        with pytest.raises(pymcnp.abc.Error) as error:
            pymcnp.Run((inp,), command='echo').run(tmp_path / 'a')
        assert 'run-00000: exit code 0, no output file' in str(error.value.body)

        (result,) = pymcnp.Run((inp,), command='echo', check=False).run(tmp_path / 'b')
        assert result.returncode == 0 and result.outp is None and not result.ok

    def test_failed_run_not_ok(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        (result,) = pymcnp.Run(_inps(inp, 1, title='EXIT'), command=fake, check=False).run(tmp_path)
        assert result.ok is False and result.returncode == 3
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run(_inps(inp, 1, title='EXIT'), command=fake, check=True).run(tmp_path)

    def test_fatal_error_in_outp_not_ok(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        (result,) = pymcnp.Run(_inps(inp, 1, title='FAIL'), command=fake, check=False).run(tmp_path)
        assert result.returncode == 0 and result.fatal_errors != [] and result.ok is False

    def test_runs_get_own_directories(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        results = pymcnp.Run(_inps(inp, 2), command=fake).run(tmp_path)
        assert [result.directory.name for result in results] == ['run-00000', 'run-00001']
        assert results[0].directory != results[1].directory
        for result in results:
            assert result.outp and result.outp.parent == result.directory and result.outp.suffix == '.outp'

    def test_directory_timestamp_per_call(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
        moments = iter([datetime.datetime(2026, 1, 1, 0, 0, 0), datetime.datetime(2026, 1, 1, 0, 0, 1)])

        class Clock:
            @staticmethod
            def today() -> datetime.datetime:
                return next(moments)

        monkeypatch.setattr(sys.modules['pymcnp.Run'].datetime, 'datetime', Clock)
        directories = []
        for _ in range(2):
            run = pymcnp.Run(_inps(inp, 1), command=fake)
            run.run(tmp_path)
            directories.append(run.directory)
        assert [d.name for d in directories] == ['pymcnp-2026-01-01--00-00-00', 'pymcnp-2026-01-01--00-00-01']

    def test_run_check_false_returns_failures(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        inps = _inps(inp, 2)
        inps[0].title = 'FAIL\n'
        results = pymcnp.Run(inps, command=fake, check=False).run(tmp_path)
        assert [result.ok for result in results] == [False, True]
        assert results[0].fatal_errors == ['surface 7 not found']

    def test_run_same_second_does_not_collide(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        for _ in range(2):
            pymcnp.Run(_inps(inp, 1), command=fake).run(tmp_path)
        assert len(list(tmp_path.glob('pymcnp-*'))) == 2

    def test_run_sets_directory(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        run = pymcnp.Run(_inps(inp, 2), command=fake)
        assert run.directory is None
        results = run.run(tmp_path)
        assert run.directory and run.directory.parent == tmp_path and run.directory.name.startswith('pymcnp-')
        assert all(result.directory.parent == run.directory for result in results)

    def test_run_without_batch_directory(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        run = pymcnp.Run(_inps(inp, 2), command=fake, names='case-{index}', batch=False)
        results = run.run(tmp_path / 'runs')
        assert run.directory == tmp_path / 'runs'
        assert [result.directory for result in results] == [tmp_path / 'runs' / 'case-0', tmp_path / 'runs' / 'case-1']
        assert all(result.ok for result in results)

        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Run(_inps(inp, 2), command=fake, names='case-{index}', batch=False).run(tmp_path / 'runs')
