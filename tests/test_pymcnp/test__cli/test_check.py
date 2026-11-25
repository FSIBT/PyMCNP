import sys
import shutil
import pathlib

import pytest

from pymcnp._cli import check

FILES: pathlib.Path = pathlib.Path(__file__).parents[3] / 'files' / 'inp'
SOURCE = 'Title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 5\n\nnps 10\n\n'


def _check(monkeypatch, capsys, *args):
    """
    Runs ``pymcnp check`` and returns its exit code and output.
    """

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', *map(str, args)])
    code = 0
    try:
        check.main()
    except SystemExit as err:
        code = err.code
    return code, capsys.readouterr().out


def test_main_valid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / 'valid_00.inp')])
    check.main()


def test_main_valid_fix(monkeypatch, tmp_path) -> None:
    path = tmp_path / 'valid.inp'
    shutil.copy(FILES / 'valid_00.inp', path)
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(path), '--fix'])
    check.main()


@pytest.mark.parametrize('name', ['warning_00.inp', 'invalid_00.inp', 'invalid_01.inp', 'invalid_02.inp', 'hello'])
def test_main_invalid(monkeypatch, name) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / name)])
    with pytest.raises(SystemExit):
        check.main()


class Test_Check_Report:
    def test_valid_file(self, monkeypatch, capsys, tmp_path) -> None:
        path = tmp_path / 'ok.inp'
        path.write_text(SOURCE)

        code, out = _check(monkeypatch, capsys, path)

        assert code == 0
        assert 'Done!' in out

    def test_missing_file_exits_2(self, monkeypatch, capsys, tmp_path) -> None:
        code, _ = _check(monkeypatch, capsys, tmp_path / 'missing.inp')

        assert code == 2

    def test_wide_line_exits_1(self, monkeypatch, capsys, tmp_path) -> None:
        path = tmp_path / 'wide.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10 $ ' + 'x' * 80))

        code, out = _check(monkeypatch, capsys, path)

        assert code == 1
        assert 'Line 7' in out
        assert 'Done!' not in out

    def test_fix_wraps_wide_line(self, monkeypatch, capsys, tmp_path) -> None:
        path = tmp_path / 'wide.inp'
        bins = ' '.join(str(10 * n) for n in range(1, 40))
        path.write_text(SOURCE.replace('nps 10', f'si1 {bins}\nnps 10'))

        code, out = _check(monkeypatch, capsys, '--fix', path)

        assert code == 0
        assert 'Done!' in out
        assert max(len(line) for line in path.read_text().split('\n')) <= 80

    def test_unparseable_card_warns_and_exits_3(self, monkeypatch, capsys, tmp_path) -> None:
        path = tmp_path / 'unknown.inp'
        path.write_text(SOURCE.replace('1 so 5', '1 so 5\n2 zzz 5'))

        code, out = _check(monkeypatch, capsys, path)

        assert code == 3
        assert 'Line 6' in out
        assert 'again' in ' '.join(out.split())
        assert 'Done!' not in out

    def test_fix_leaves_unparseable_file_alone(self, monkeypatch, capsys, tmp_path) -> None:
        path = tmp_path / 'unknown.inp'
        text = SOURCE.replace('1 so 5', '1 so 5\n2 zzz 5')
        path.write_text(text)

        code, out = _check(monkeypatch, capsys, '--fix', path)

        assert code == 3
        assert 'Not reformatting' in out
        assert path.read_text() == text

    def test_diff_shows_wrapped_line(self, monkeypatch, capsys, tmp_path) -> None:
        path = tmp_path / 'wide.inp'
        bins = ' '.join(str(10 * n) for n in range(1, 40))
        path.write_text(SOURCE.replace('nps 10', f'si1 {bins}\nnps 10'))

        code, out = _check(monkeypatch, capsys, '--diff', path)

        assert code == 1
        assert f'-si1 {bins}' in out
        assert '+si1 10 20' in out
        assert ' &' in out
        assert path.read_text().count('\n') == SOURCE.count('\n') + 1

    def test_diff_of_formatted_file_prints_nothing(self, monkeypatch, capsys, tmp_path) -> None:
        path = tmp_path / 'ok.inp'
        shutil.copy(FILES / 'valid_00.inp', path)
        # Format first so the diff is empty.
        _check(monkeypatch, capsys, '--fix', path)

        code, out = _check(monkeypatch, capsys, '--diff', path)

        assert code == 0
        assert '@@' not in out
