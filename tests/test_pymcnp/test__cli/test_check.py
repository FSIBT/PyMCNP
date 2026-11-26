import sys
import warnings
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


@pytest.mark.parametrize('name, code', [('warning_00.inp', 1), ('invalid_00.inp', 3), ('invalid_01.inp', 3), ('invalid_02.inp', 3), ('hello', 2)])
def test_main_invalid(monkeypatch, name, code) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', str(FILES / name)])
    with pytest.raises(SystemExit) as error:
        check.main()
    assert error.value.code == code


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

    @pytest.mark.parametrize(
        'line, number',
        [
            # A full-line comment and a `$` comment that `--fix` cannot rewrap.
            ('c ' + 'c' * 80, 8),
            ('nps 10 $ ' + 'x' * 80, 7),
        ],
        ids=['comment', 'dollar'],
    )
    @pytest.mark.parametrize('fix', [[], ['--fix']])
    def test_fix_reports_lines_it_cannot_shorten(self, monkeypatch, capsys, tmp_path, line, number, fix) -> None:
        # Each wide line is reported once: not by the parser's warning, and with --fix only after fixing.
        path = tmp_path / 'wide.inp'
        path.write_text(SOURCE.replace('nps 10', line if line.startswith('nps') else f'nps 10\n{line}'))

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            code, out = _check(monkeypatch, capsys, *fix, path)

        assert code == 1
        assert [str(warning.message) for warning in caught] == []
        out = ' '.join(out.replace('│', '').split())
        assert out.count(f'Line {number}:') == 1
        assert ('cannot shorten' in out) == bool(fix)
        assert 'Done!' not in out
        assert max(len(text) for text in path.read_text().split('\n')) > 80

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


@pytest.mark.parametrize('options', [['--fix'], ['--diff'], ['--fix', '--diff']])
def test_latin_1_file_warns_once_and_fix_writes_utf8(monkeypatch, capsys, tmp_path, options) -> None:
    # A wide card line, so --fix rewrites the file; the warning is shown once per command, not per read.
    path = tmp_path / 'latin1.inp'
    path.write_bytes(SOURCE.replace('Title', 'Titel M\xfcller').replace('nps 10', 'nps 10 $' + ' x' * 40).encode('latin-1'))
    from pymcnp._cli import main

    # Through ``pymcnp``, which prints warnings as panels.
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'check', *options, str(path)])
    with pytest.raises(SystemExit):
        main.main()
    out = capsys.readouterr()
    assert (out.out + out.err).count('not UTF-8') == 1
    if '--fix' in options:
        assert path.read_bytes().startswith('Titel Müller\n'.encode('utf-8'))
    else:
        assert path.read_bytes().startswith(b'Titel M\xfcller\n')


def test_fix_of_a_latin_1_file_warns_once(tmp_path) -> None:
    import pymcnp

    path = tmp_path / 'latin1.inp'
    path.write_bytes(SOURCE.replace('Title', 'Titel M\xfcller').encode('latin-1'))
    with pytest.warns(pymcnp.abc.Warning, match='not UTF-8') as records:
        assert pymcnp.Check(path).fix() == []
    assert len([record for record in records if 'not UTF-8' in str(record.message)]) == 1
    assert path.read_text(encoding='utf-8').startswith('Titel Müller\n')
