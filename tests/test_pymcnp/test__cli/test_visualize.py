import os
import pathlib


class Test_Main:
    class Test_Main:
        def test_valid(self):
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"}')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cells')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surfaces')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cells --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surfaces --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cell=1')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surface=1')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cell=1 --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surface=1 --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cells-skip=1')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surfaces-skip=1')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --cells-skip=1 --pdf')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --surfaces-skip=1 --pdf')

        def test_invalid(self):
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_00.inp"}')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_01.inp"}')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_02.inp"}')
            os.system(f'pymcnp visualize {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "todo_41.inp"}')
            os.system('pymcnp visualize hello')


class Test_Visualize_Arguments:
    INP = 'c title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 1\n\nnps 1\n'

    def _run(self, monkeypatch, tmp_path, *args):
        from pymcnp._cli import visualize

        path = tmp_path / 'in.inp'
        path.write_text(self.INP)
        monkeypatch.setattr('sys.argv', ['pymcnp', 'visualize', str(path), *args])

        visualize.main()

    def test_short_options_are_not_ambiguous(self, monkeypatch, tmp_path):
        self._run(monkeypatch, tmp_path, '-c', '1')
        self._run(monkeypatch, tmp_path, '-s', '1')

    def test_skip_options_write_pdfs(self, monkeypatch, tmp_path):
        self._run(monkeypatch, tmp_path, '--cells-skip=1', '--pdf')
        self._run(monkeypatch, tmp_path, '--surfaces-skip=1', '--pdf')

    def test_listed_options_write_pdfs(self, monkeypatch, tmp_path):
        self._run(monkeypatch, tmp_path, '--cell=1', '--pdf')
        self._run(monkeypatch, tmp_path, '--surface=1', '--pdf')

    def test_unknown_number_exits(self, monkeypatch, tmp_path):
        import pytest

        with pytest.raises(SystemExit) as err:
            self._run(monkeypatch, tmp_path, '-c', '999')

        assert err.value.code == 2

    def test_options_before_input(self, monkeypatch, tmp_path):
        from pymcnp._cli import visualize

        path = tmp_path / 'in.inp'
        path.write_text(self.INP)

        for args in (['-s', '1'], ['-c', '1,2'], ['--cell=1', '--cell=2'], ['--surfaces-skip=1']):
            monkeypatch.setattr('sys.argv', ['pymcnp', 'visualize', *args, str(path)])
            visualize.main()
