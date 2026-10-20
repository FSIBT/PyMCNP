import sys
import shutil
import pathlib

import pytest

import pymcnp

FAKE = """#!{python}
import sys, pathlib
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
    path.write_text(FAKE.format(python=sys.executable))
    path.chmod(0o755)
    return str(path)


def _inps(inp: pymcnp.Inp, count: int, title: str = 'T') -> list[pymcnp.Inp]:
    inps = []
    for i in range(count):
        copy = pymcnp.Inp.from_mcnp(inp.to_mcnp())[0]
        copy.title = f'{title} {i}\n'
        inps.append(copy)
    return inps


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

    def test_hooks_valid(self, run: pymcnp.Run, tmp_path: pathlib.Path) -> None:
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
                calls.append('batch')

        with pytest.raises(pymcnp.abc.Error) as error:
            Hooked(inps, command=fake).run(tmp_path)

        assert 'run-00001' in str(error.value.body) and 'surface 7 not found' in str(error.value.body)
        assert sorted(calls) == [0, 2]  # the other runs finished, no batch hook
        assert len(list(next(tmp_path.glob('pymcnp-*')).glob('run-*'))) == 3

    def test_run_exit_code_is_a_failure(self, inp: pymcnp.Inp, fake: str, tmp_path: pathlib.Path) -> None:
        inps = _inps(inp, 1, title='EXIT')
        with pytest.raises(pymcnp.abc.Error, match='Run failed'):
            pymcnp.Run(inps, command=fake).run(tmp_path)

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


@pytest.mark.skipif(shutil.which('mcnp6') is None, reason='mcnp6 not installed')
def test_run_mcnp6(tmp_path: pathlib.Path) -> None:
    source = pathlib.Path(__file__).parents[2] / 'files' / 'inp' / 'valid_00.inp'
    inp, _ = pymcnp.Inp.from_file(source)
    inp.nps = 50
    (result,) = pymcnp.Run([inp], check=False).run(tmp_path)
    assert result.outp and result.ptrac is None or result.outp
