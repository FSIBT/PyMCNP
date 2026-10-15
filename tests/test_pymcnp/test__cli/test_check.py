import os
import pathlib
import subprocess

SOURCE = 'Title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 5\n\nnps 10\n\n'


def _check(*args):
    return subprocess.run(['pymcnp', 'check', *map(str, args)], capture_output=True, text=True, check=False)


class Test_Main:
    class Test_Main:
        def test_valid(self):
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"}')
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "valid_00.inp"} --fix')

        def test_invalid(self):
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_00.inp"}')
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_01.inp"}')
            os.system(f'pymcnp check {pathlib.Path(__file__).parent.parent.parent.parent / "files" / "inp" / "invalid_02.inp"}')
            os.system('pymcnp check hello')


class Test_Check_Report:
    def test_valid_file(self, tmp_path):
        path = tmp_path / 'ok.inp'
        path.write_text(SOURCE)

        result = _check(path)

        assert result.returncode == 0
        assert 'Done!' in result.stdout

    def test_wide_line_exits_1_and_fix_wraps_it(self, tmp_path):
        path = tmp_path / 'wide.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10 $ ' + 'x' * 80))

        result = _check(path)

        assert result.returncode == 1
        assert 'Line 7' in result.stdout
        assert 'Done!' not in result.stdout

    def test_unparseable_card_warns_and_exits_3(self, tmp_path):
        path = tmp_path / 'unknown.inp'
        path.write_text(SOURCE.replace('1 so 5', '1 so 5\n2 zzz 5'))

        result = _check(path)

        assert result.returncode == 3
        assert 'Line 6' in result.stdout
        assert 'again' in result.stdout
        assert 'Done!' not in result.stdout

    def test_fix_leaves_unparseable_file_alone(self, tmp_path):
        path = tmp_path / 'unknown.inp'
        text = SOURCE.replace('1 so 5', '1 so 5\n2 zzz 5')
        path.write_text(text)

        result = _check('--fix', path)

        assert result.returncode == 3
        assert path.read_text() == text

    def test_diff_shows_changes(self, tmp_path):
        path = tmp_path / 'style.inp'
        path.write_text(SOURCE.replace('nps 10', 'NPS   10'))

        result = _check('--diff', path)

        assert result.returncode == 0
        assert '-NPS   10' in result.stdout
