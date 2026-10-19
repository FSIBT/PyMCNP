import sys
import pathlib
import subprocess

import pytest

from pymcnp._cli import check

SOURCE = 'Title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 5\n\nnps 10\n\n'


def _check(*args):
    return subprocess.run(['pymcnp', 'check', *map(str, args)], capture_output=True, text=True, check=False)


def test_main_valid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp')])
    check.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--fix'])
    check.main()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit):
        check.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_01.inp')])
    with pytest.raises(SystemExit):
        check.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_02.inp')])
    with pytest.raises(SystemExit):
        check.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', 'hello'])
    with pytest.raises(SystemExit):
        check.main()


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

    def test_diff_shows_wrapped_line(self, tmp_path):
        path = tmp_path / 'wide.inp'
        bins = ' '.join(str(10 * n) for n in range(1, 40))
        path.write_text(SOURCE.replace('nps 10', f'si1 {bins}\nnps 10'))

        result = _check('--diff', path)

        assert result.returncode == 1
        assert f'-si1 {bins}' in result.stdout
        assert '+si1 10 20' in result.stdout
        assert ' &' in result.stdout
