"""
Every command exits with the codes of one table: 0 success; 1 the input or
output has problems, or the command failed; 2 usage error, or a file that does
not exist or cannot be read as text; 3 PyMCNP cannot parse all of a file. A
file gets the same code from every command that reads it.
"""

import os
import sys
import shutil
import pathlib

import pandas
import pytest
import matplotlib.pyplot

import pymcnp
from pymcnp._cli import main

from ...console import plain


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'

# The OUTP fixtures hold tallies PyMCNP cannot parse.
pytestmark = pytest.mark.filterwarnings('ignore:Tally not parsed:pymcnp.abc.Warning')

# Cell card 2 parses only in part, so nothing after it can be read.
BAD_CELL = 'title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0 foo=3\n\n1 so 5\n\nnps 10\n'

COMMANDS = [
    ['check'],
    ['convert', 'outp', '--csv'],
    ['convert', 'ptrac', '--parquet'],
    ['convert', 'meshtal', '--csv'],
    ['plot', '--pdf', '{file}', '1'],
    ['visualize', '--pdf'],
    ['run'],
]


def _args(command: list[str], file: pathlib.Path) -> list[str]:
    if '{file}' in command:
        return [str(file) if arg == '{file}' else arg for arg in command]
    return [*command, str(file)]


def _run(monkeypatch, capsys, *args: str) -> tuple[int, str]:
    """
    Runs ``pymcnp`` as from the shell, returning its exit code and output with the panel borders and line breaks removed.
    """

    monkeypatch.setattr(sys, 'argv', ['pymcnp', *args])
    try:
        main.main()
    except SystemExit as exit:
        code = 0 if exit.code is None else exit.code
    else:
        code = 0
    out = capsys.readouterr()
    text = plain(out.out + out.err)
    assert 'Traceback' not in text
    return code, text


@pytest.mark.parametrize('args', [['nosuch'], ['check'], ['check', '--bogus', 'a.inp'], ['convert', 'outp', 'a.outp'], ['plot', 'a.outp'], ['run'], ['visualize']])
def test_usage_error_exits_2(monkeypatch, capsys, args) -> None:
    code, text = _run(monkeypatch, capsys, *args)
    assert code == 2
    assert 'Usage:' in text


def test_help(monkeypatch, capsys) -> None:
    assert _run(monkeypatch, capsys, 'help') == (0, ' '.join(str(main.__doc__).split()))
    code, text = _run(monkeypatch, capsys, 'help', 'convert')
    assert code == 0 and 'pymcnp convert outp' in text


def test_help_unknown_command_exits_2(monkeypatch, capsys) -> None:
    code, text = _run(monkeypatch, capsys, 'help', 'hello')
    assert code == 2
    assert 'Error: No command hello; the commands are run, check, visualize, convert, plot.' in text


@pytest.mark.parametrize('command', COMMANDS)
def test_missing_file_exits_2(monkeypatch, capsys, tmp_path: pathlib.Path, command) -> None:
    monkeypatch.chdir(tmp_path)
    code, text = _run(monkeypatch, capsys, *_args(command, pathlib.Path('nosuch')))
    assert code == 2
    assert 'Error: nosuch: no such file.' in text


@pytest.mark.parametrize('command', COMMANDS)
def test_directory_exits_2(monkeypatch, capsys, tmp_path: pathlib.Path, command) -> None:
    monkeypatch.chdir(tmp_path)
    pathlib.Path('folder').mkdir()
    code, text = _run(monkeypatch, capsys, *_args(command, pathlib.Path('folder')))
    assert code == 2
    assert 'Error: folder: not a file.' in text


@pytest.mark.parametrize('command', COMMANDS)
def test_binary_file_exits_2(monkeypatch, capsys, tmp_path: pathlib.Path, command) -> None:
    # E.g., a PTRAC file MCNP wrote in binary, its default: the hint is for PTRAC only.
    monkeypatch.chdir(tmp_path)
    pathlib.Path('binary').write_bytes(b'\x01\xff\x00\x80 binary PTRAC\n')
    code, text = _run(monkeypatch, capsys, *_args(command, pathlib.Path('binary')))
    assert code == 2
    hint = ' PyMCNP reads text PTRAC files only: have MCNP write one with the PTRAC option FILE=ASC.'
    assert text == f'Error: binary: not a text file (a NUL byte at byte offset 2), so PyMCNP cannot read it.{hint if "ptrac" in command else ""}'


@pytest.mark.parametrize('command', COMMANDS)
def test_utf_16_file_exits_2(monkeypatch, capsys, tmp_path: pathlib.Path, command) -> None:
    monkeypatch.chdir(tmp_path)
    pathlib.Path('utf16').write_bytes('title\n'.encode('utf-16'))
    code, text = _run(monkeypatch, capsys, *_args(command, pathlib.Path('utf16')))
    assert code == 2
    assert text == 'Error: utf16: UTF-16 text, which PyMCNP does not read; save the file as UTF-8.'


@pytest.mark.parametrize(
    'command, fixture, word, line',
    [
        (['check'], 'inp/valid_00.inp', 'Problem', 1),
        (['convert', 'outp', '--csv'], 'outp/valid_39.outp', 'regolith', 39),
        (['convert', 'ptrac', '--parquet'], 'ptrac/valid_38.ptrac', 'regolith', 3),
        (['convert', 'meshtal', '--csv'], 'meshtal/valid_41.meshtal', 'regolith', 2),
        (['plot', '--pdf', '{file}', '14'], 'outp/valid_39.outp', 'regolith', 39),
        (['visualize', '--pdf', '--cell=81023'], 'inp/valid_00.inp', 'Problem', 1),
        (['run', '--command=nosuchmcnp6'], 'inp/valid_00.inp', 'Problem', 1),
    ],
)
def test_latin_1_file_warns(monkeypatch, capsys, tmp_path: pathlib.Path, command, fixture, word, line) -> None:
    # Text, but not UTF-8, e.g., saved as cp1252 on Windows: read as Latin-1 with a warning, which does not change the
    # exit code.
    monkeypatch.chdir(tmp_path)
    text = (FILES / fixture).read_text(encoding='utf-8').replace(word, word.replace('o', 'ö', 1).replace('e', 'é', 1), 1)
    pathlib.Path('utf8').write_bytes(text.encode('utf-8'))
    pathlib.Path('latin1').write_bytes(text.encode('cp1252'))
    code_utf8, text_utf8 = _run(monkeypatch, capsys, *_args(command, pathlib.Path('utf8')))
    code, text = _run(monkeypatch, capsys, *_args(command, pathlib.Path('latin1')))
    warning = f'Warning: File is not UTF-8 text, so PyMCNP reads it as Latin-1. latin1, line {line}'
    assert code == code_utf8
    assert text.count(warning) == 1
    assert text.replace(warning, '').replace('latin1', 'utf8').split() == text_utf8.split()


@pytest.mark.skipif(os.name == 'nt' or (hasattr(os, 'geteuid') and os.geteuid() == 0), reason='needs file permissions that the user cannot override')
@pytest.mark.parametrize('command', COMMANDS)
def test_unreadable_file_exits_2(monkeypatch, capsys, tmp_path: pathlib.Path, command) -> None:
    monkeypatch.chdir(tmp_path)
    path = pathlib.Path('locked')
    path.write_text('title\n')
    path.chmod(0)
    try:
        code, text = _run(monkeypatch, capsys, *_args(command, path))
    finally:
        path.chmod(0o644)
    assert code == 2
    assert 'locked: cannot read the file: Permission denied.' in text


@pytest.mark.parametrize('command', [['check'], ['visualize', '--pdf'], ['run']])
def test_cell_card_that_does_not_parse_exits_3(monkeypatch, capsys, tmp_path: pathlib.Path, command) -> None:
    # As `pymcnp check` does: the card is named with its line.
    monkeypatch.chdir(tmp_path)
    pathlib.Path('bad.inp').write_text(BAD_CELL)
    code, text = _run(monkeypatch, capsys, *command, 'bad.inp', *(['--command=echo', f'--path={tmp_path}'] if command == ['run'] else []))
    assert code == 3
    assert ('Line 3: PyMCNP cannot parse this card' if command == ['check'] else 'bad.inp, line 3: PyMCNP cannot parse this card') in text
    assert "Expected end of card at 'foo=3'." in text
    assert not list(tmp_path.glob('pymcnp-*')) and not list(tmp_path.glob('*.pdf'))


def test_data_card_that_parses_in_part_exits_3(monkeypatch, capsys, tmp_path: pathlib.Path, fake_mcnp: str) -> None:
    # valid_07.inp has a tally PyMCNP parses only in part; this was "Expected Inp.blank_2", exit 1.
    code, text = _run(monkeypatch, capsys, 'run', str(FILES / 'inp' / 'valid_07.inp'), f'--command={fake_mcnp}', f'--path={tmp_path}')
    assert code == 3
    assert 'line 18: PyMCNP cannot parse the card "f4:p (11<16[-10:10 -10:10 -10:10]<17)"' in text
    assert 'Not running' in text and not list(tmp_path.glob('pymcnp-*'))


def test_check_exit_codes(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    code, text = _run(monkeypatch, capsys, 'check', str(FILES / 'inp' / 'valid_00.inp'))
    assert (code, text) == (0, 'Info: Done!')

    wide = tmp_path / 'wide.inp'
    wide.write_text(BAD_CELL.replace(' foo=3', '').replace('nps 10', 'c ' + 'x' * 90 + '\nnps 10'))
    code, text = _run(monkeypatch, capsys, 'check', str(wide))
    assert code == 1
    assert 'Line 7: Line exceeds 80 characters maximum length (92 columns).' in text


def test_convert_exit_codes(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    outp = tmp_path / 'run.outp'
    shutil.copy(FILES / 'outp' / 'valid_39.outp', outp)
    code, text = _run(monkeypatch, capsys, 'convert', 'outp', '--csv', str(outp))
    assert code == 0
    assert f'Wrote {tmp_path / "run.outp.csv"}'.replace(' ', '') in text.replace(' ', '') and 'Done!' in text
    assert len(pandas.read_csv(tmp_path / 'run.outp.csv')) > 0

    # An INP file is not an OUTP file: PyMCNP cannot parse it as one.
    code, text = _run(monkeypatch, capsys, 'convert', 'outp', '--csv', str(FILES / 'inp' / 'valid_00.inp'))
    assert code == 3
    assert 'PyMCNP cannot parse this file:' in text


def test_convert_with_only_unparsed_tallies_exits_3(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    # valid_01.outp parses, but its only tally is in a layout PyMCNP cannot parse yet: write no empty CSV.
    outp = tmp_path / 'valid_01.outp'
    shutil.copy(FILES / 'outp' / 'valid_01.outp', outp)
    monkeypatch.chdir(tmp_path)
    code, text = _run(monkeypatch, capsys, 'convert', 'outp', '--csv', 'valid_01.outp')
    assert code == 3
    assert 'Error: valid_01.outp: nothing to convert; no file written.' in text
    assert sorted(path.name for path in tmp_path.iterdir()) == ['valid_01.outp']


def test_convert_with_nothing_parsed_but_a_remainder_exits_3(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    outp = tmp_path / 'valid_01.outp'
    shutil.copy(FILES / 'outp' / 'valid_01.outp', outp)
    from_file = pymcnp.Outp.from_file
    monkeypatch.setattr(pymcnp.Outp, 'from_file', lambda file: (from_file(file)[0], 'garbage [here]\n'))
    code, text = _run(monkeypatch, capsys, 'convert', 'outp', '--parquet', str(outp))
    assert code == 3
    assert 'nothing to convert; no file written.' in text
    assert sorted(path.name for path in tmp_path.iterdir()) == ['valid_01.outp']


def test_convert_outp_and_ptrac_of_one_run_write_two_files(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    shutil.copy(FILES / 'outp' / 'valid_39.outp', tmp_path / 'run.outp')
    shutil.copy(FILES / 'ptrac' / 'valid_38.ptrac', tmp_path / 'run.ptrac')
    assert _run(monkeypatch, capsys, 'convert', 'outp', '--csv', str(tmp_path / 'run.outp'))[0] == 0
    assert _run(monkeypatch, capsys, 'convert', 'ptrac', '--csv', str(tmp_path / 'run.ptrac'))[0] == 0

    outp, ptrac = pandas.read_csv(tmp_path / 'run.outp.csv'), pandas.read_csv(tmp_path / 'run.ptrac.csv')
    assert 'counts' in outp.columns and 'counts' not in ptrac.columns
    assert len(ptrac) == len(pymcnp.Ptrac.from_file(tmp_path / 'run.ptrac')[0].to_dataframe())


def test_plot_exit_codes(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    outp = tmp_path / 'run.outp'
    shutil.copy(FILES / 'outp' / 'valid_39.outp', outp)

    code, text = _run(monkeypatch, capsys, 'plot', '--pdf', str(outp), '21')
    assert (code, text) == (0, 'Info: Done!')
    assert (tmp_path / 'run.pdf').stat().st_size > 0

    # A tally that is not in the file is a usage error.
    code, text = _run(monkeypatch, capsys, 'plot', '--pdf', str(outp), '999')
    assert code == 2
    assert "Error: Tally not found. number='999'" in text

    # A tally in the file, in a layout PyMCNP cannot parse yet, as `convert` says.
    shutil.copy(FILES / 'outp' / 'valid_01.outp', tmp_path / 'valid_01.outp')
    code, text = _run(monkeypatch, capsys, 'plot', '--pdf', str(tmp_path / 'valid_01.outp'), '4')
    assert code == 3
    assert "Error: Tally not parsed. number='4'" in text
    assert not (tmp_path / 'valid_01.pdf').exists()

    code, text = _run(monkeypatch, capsys, 'plot', '--pdf', str(FILES / 'inp' / 'valid_00.inp'), '1')
    assert code == 3
    matplotlib.pyplot.close('all')


def test_run_exit_codes(monkeypatch, capsys, tmp_path: pathlib.Path, fake_mcnp: str) -> None:
    code, text = _run(monkeypatch, capsys, 'run', str(FILES / 'inp' / 'valid_00.inp'), f'--command={fake_mcnp}', f'--path={tmp_path}')
    assert (code, text) == (0, 'Info: Done!')
    (outp,) = tmp_path.glob('pymcnp-*/run-00000/run-00000.outp')
    assert outp.read_text() == 'ok\n'

    # The missing executable is named.
    code, text = _run(monkeypatch, capsys, 'run', str(FILES / 'inp' / 'valid_00.inp'), '--command=nosuchmcnp6')
    assert code == 1
    assert "Error: MCNP command not found: nosuchmcnp6 'nosuchmcnp6' is not an executable file or on the PATH." in text

    # Every card parses, but two cells have the same number.
    twice = tmp_path / 'twice.inp'
    twice.write_text('title\n1 0 -1\n1 0 1\n\n1 so 5\n\nnps 10\n')
    code, text = _run(monkeypatch, capsys, 'run', str(twice), f'--command={fake_mcnp}', f'--path={tmp_path / "not"}')
    assert code == 3
    assert "PyMCNP cannot parse this file: Invalid value. card.j='1'" in text
    assert not (tmp_path / 'not').exists()


def test_run_failed_exits_1(monkeypatch, capsys, tmp_path: pathlib.Path, fake_mcnp_fail: str) -> None:
    code, text = _run(monkeypatch, capsys, 'run', str(FILES / 'inp' / 'valid_00.inp'), f'--command={fake_mcnp_fail}', f'--path={tmp_path}')
    assert code == 1
    assert 'Error: Run failed.' in text


@pytest.mark.parametrize('option', ['-c abc', '--cell=1,x', '-s abc', '--cells-skip=abc', '--surfaces-skip=1;2'])
def test_visualize_numbers_that_are_not_numbers_exit_2(monkeypatch, capsys, option: str) -> None:
    code, text = _run(monkeypatch, capsys, 'visualize', '--pdf', *option.split(), str(FILES / 'inp' / 'valid_00.inp'))
    assert code == 2
    assert 'expected numbers separated by commas, e.g., 1,2, not' in text


def test_visualize_exit_codes(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    code, text = _run(monkeypatch, capsys, 'visualize', '--pdf', '--cell=81023', str(FILES / 'inp' / 'valid_00.inp'))
    assert code == 2
    assert 'Error: --cell: no such cell: 81023.' in text

    # A geometry PyMCNP cannot visualize.
    def fail(*args, **kwargs):
        raise pymcnp.abc.Error('Cannot visualize.', 'body')

    monkeypatch.setattr(pymcnp.Visualize, 'to_pdf_cells', fail)
    inp = tmp_path / 'valid_00.inp'
    shutil.copy(FILES / 'inp' / 'valid_00.inp', inp)
    code, text = _run(monkeypatch, capsys, 'visualize', '--pdf', '--cells', str(inp))
    assert code == 1
    assert 'Error: Cannot visualize. body' in text


@pytest.mark.parametrize(
    'source',
    [
        pytest.param('title\n1 0 -1\n1 0 1\n\n1 so 5\n\nnps 10\n', id='duplicate cells'),
        pytest.param('title\n1 0 -1\n1 0 1\n\n1 so 5\n\nnps 10\nqqq 1\n', id='duplicate cells and a card that does not parse'),
        pytest.param(BAD_CELL, id='cell card'),
        pytest.param('title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 5\n\nnps 10\nqqq 1\n', id='data card', marks=pytest.mark.render),  # `visualize` draws the cards before it
        pytest.param('title\n1 0 -1 imp:n=1\n', id='no surfaces'),
    ],
)
def test_same_file_same_code(monkeypatch, capsys, tmp_path: pathlib.Path, fake_mcnp: str, source: str) -> None:
    # check, run, visualize, convert and plot each exit 3 for an input PyMCNP cannot parse.
    monkeypatch.chdir(tmp_path)
    pathlib.Path('bad.inp').write_text(source)
    commands = [
        ['check', 'bad.inp'],
        ['run', 'bad.inp', f'--command={fake_mcnp}', f'--path={tmp_path}'],
        ['visualize', '--pdf', 'bad.inp'],
        ['convert', 'outp', '--csv', 'bad.inp'],
        ['plot', '--pdf', 'bad.inp', '1'],
    ]
    codes = {command[0]: _run(monkeypatch, capsys, *command)[0] for command in commands}
    assert codes == dict.fromkeys(codes, 3)
    # Nothing run, converted or plotted; `visualize` draws the cards before a data card that does not parse.
    assert not list(tmp_path.glob('pymcnp-*')) and not list(tmp_path.glob('bad.inp.*')) and not (tmp_path / 'bad.pdf').exists()
    matplotlib.pyplot.close('all')


def test_convert_says_mcnp_stopped_with_a_fatal_error(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    # MCNP stopped before running histories, so the file has no tallies: say why.
    outp = tmp_path / 'valid_26.outp'
    shutil.copy(FILES / 'outp' / 'valid_26.outp', outp)
    monkeypatch.chdir(tmp_path)
    code, text = _run(monkeypatch, capsys, 'convert', 'outp', '--csv', 'valid_26.outp')
    assert code == 1
    assert 'valid_26.outp: nothing to convert; no file written.' in text
    assert 'MCNP stopped with a fatal error: cross-section tables missing for zaid = 6012.60c' in text


def test_convert_names_the_first_three_fatal_errors(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    outp = tmp_path / 'valid_25.outp'
    shutil.copy(FILES / 'outp' / 'valid_25.outp', outp)
    code, text = _run(monkeypatch, capsys, 'convert', 'outp', '--parquet', str(outp))
    assert code == 1
    assert 'MCNP stopped with 40 fatal errors, e.g.:' in text
    assert text.count('is not a legal data symbol.') == 1


@pytest.mark.parametrize(
    'args, message',
    [
        (['convert', '--partquet', 'outp'], 'Unknown option --partquet; did you mean --parquet?'),
        (['convert', 'outp', '--partquet', 'outp'], 'Unknown option --partquet; did you mean --parquet?'),
        (['convert', '--parquet', 'outp.txt'], 'pymcnp convert needs outp, ptrac or meshtal, not outp.txt.'),
        (['convert', 'otup', '--csv', 'a'], 'pymcnp convert needs outp, ptrac or meshtal, not otup; did you mean outp?'),
        (['convert', 'outp', 'a.outp'], 'Give --csv or --parquet.'),
        (['convert', 'outp', '--csv', '--parquet', 'a.outp'], 'Give only one of --csv and --parquet.'),
        (['convert', 'outp', '--csv'], 'pymcnp convert outp needs <file>.'),
        (['check', '--fxi', 'a.inp'], 'Unknown option --fxi; did you mean --fix?'),
        (['check'], 'pymcnp check needs <inp>.'),
        (['check', 'a.inp', 'b.inp'], 'Unexpected argument b.inp.'),
        (['visualize', '-q', 'a.inp'], 'Unknown option -q.'),
        (['plot', 'a.outp'], 'pymcnp plot needs <number>.'),
        (['run'], 'pymcnp run needs <inp>.'),
        (['nosuch'], 'pymcnp needs run, check, visualize, convert, plot or help, not nosuch.'),
        ([], 'pymcnp needs run, check, visualize, convert, plot or help.'),
        (['--bogus'], 'Unknown option --bogus.'),
    ],
)
def test_usage_error_says_what_is_wrong(monkeypatch, capsys, args, message) -> None:
    code, text = _run(monkeypatch, capsys, *args)
    assert code == 2
    assert f'Error: {message}' in text
    assert 'Usage:' in text
    assert 'unmatched' not in text


def test_options_may_be_abbreviated_or_bundled(monkeypatch, capsys, tmp_path: pathlib.Path) -> None:
    # docopt accepts a unique prefix of a long option and bundled short options; do not call them unknown.
    code, text = _run(monkeypatch, capsys, 'check', '--fi', '-fd')
    assert code == 2
    assert 'Error: pymcnp check needs <inp>.' in text
