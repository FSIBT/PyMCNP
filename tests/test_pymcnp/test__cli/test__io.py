import pathlib

import pytest

from pymcnp._cli import _io


@pytest.mark.parametrize(
    'path, ext, i, expected',
    [
        ('run/example_00.outp', 'csv', None, 'run/example_00.csv'),
        ('run/example_00.inp', 'pdf', 'cells', 'run/example_00-cells.pdf'),
        ('run/a.b.outp', 'csv', None, 'run/a.b.csv'),
        # MCNP's default output names have no extension.
        ('run/outp', 'csv', None, 'run/outp.csv'),
        ('run/ptrac', 'parquet', None, 'run/ptrac.parquet'),
        ('outp', 'pdf', None, 'outp.pdf'),
        ('run.d/meshtal', 'csv', None, 'run.d/meshtal.csv'),
        (pathlib.Path('run.d/inp'), 'pdf', 'surface_1', 'run.d/inp-surface_1.pdf'),
    ],
)
def test_get_outfile(path, ext, i, expected) -> None:
    assert _io.get_outfile(path, ext, i) == pathlib.Path(expected)


def _warning(capsys) -> str:
    # Panels wrap lines, so compare without whitespace.
    return ''.join(capsys.readouterr().out.replace('│', '').split())


def _squeeze(text: str) -> str:
    return ''.join(text.split())


def test_partly_parsed_inp_names_the_line(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    # As `pymcnp check` does: comment cards are skipped, and the card's first line is named, not the remainder's.
    # A short relative path, since panels cut long words short.
    monkeypatch.chdir(tmp_path)
    path = pathlib.Path('partly.inp')
    path.write_text('title\n1 0 -1\n\n1 so 1\n\nc a comment\nnps 1\nprdmp j j -1\nc after\n')

    assert _io.partly_parsed(path, 'c a comment\nnps 1\nprdmp j j -1\nc after\n')
    assert _squeeze(f'{path}, line 8: PyMCNP cannot parse the card "prdmp j j -1", so it and every card after it are missing.') in _warning(capsys)


def test_partly_parsed_inp_without_a_located_card(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    # If every card parses on its own, the warning quotes the remainder, as before.
    # A short relative path, since panels cut long words short.
    monkeypatch.chdir(tmp_path)
    path = pathlib.Path('clean.inp')
    path.write_text('title\n1 0 -1\n\n1 so 1\n\nnps 1\n')

    assert _io.partly_parsed(path, '\nleft [over]\n')
    assert _squeeze(f'{path}: PyMCNP cannot parse the card "left [over]", so it and every card after it are missing.') in _warning(capsys)


@pytest.mark.parametrize(
    'remainder, expected',
    [
        # The remainder is the end of the file: its first line that is not blank is named.
        ('\n\nc 3\n \nd 4\n', ', line 4: PyMCNP cannot parse the line "c 3"'),
        (' \nd 4\n', ', line 6: PyMCNP cannot parse the line "d 4"'),
        # It may start inside a line.
        ('3\n \nd 4\n', ', line 4: PyMCNP cannot parse the line "3"'),
        # Otherwise there is no line number.
        ('x [1]\n', ': PyMCNP cannot parse the line "x [1]"'),
    ],
)
def test_partly_parsed_lines(monkeypatch, capsys, tmp_path: pathlib.Path, remainder: str, expected: str) -> None:
    # A short relative path, since panels cut long words short.
    monkeypatch.chdir(tmp_path)
    path = pathlib.Path('outp')
    path.write_text('a 1\nb 2\n\nc 3\n \nd 4\n')

    assert _io.partly_parsed(path, remainder, 'line')
    assert _squeeze(f'{path}{expected}, so it and every line after it are missing.') in _warning(capsys)


def test_partly_parsed_empty_remainder(capsys, tmp_path: pathlib.Path) -> None:
    assert not _io.partly_parsed(tmp_path / 'missing.inp', ' \n')
    assert not _warning(capsys)
