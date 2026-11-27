import re
import shutil
import warnings
import dataclasses
import pathlib
import subprocess

import pytest

import pymcnp
from pymcnp.Inp import _wrap

EXAMPLES = pathlib.Path(__file__).parents[2] / 'examples'
INPS = sorted(EXAMPLES.glob('example_*.inp'))
IDS = [path.stem for path in INPS]
FILES = pathlib.Path(__file__).parents[2] / 'files' / 'inp'


def _parses_fully(path):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        try:
            return pymcnp.Inp.from_file(path)[1] == ''
        except pymcnp.abc.Error:
            return False


# Every input fixture and example that PyMCNP parses completely.
COMPLETE = [path for path in sorted(FILES.glob('*.inp')) + INPS if _parses_fully(path)]


def _canonical(symbol):
    """
    Describes a parse result by its kinds and values, without the whitespace between its constituents.
    """

    if isinstance(symbol, list):
        return [_canonical(item) for item in symbol]
    if dataclasses.is_dataclass(symbol):
        return (type(symbol).__name__, {field.name: _canonical(getattr(symbol, field.name)) for field in dataclasses.fields(symbol) if field.name != 'spaces'})
    return (type(symbol).__name__, str(symbol))


def _fast(source):  # pragma: no cover (only with --run-mcnp)
    """Cuts the run to 2000 histories with a fixed seed."""

    source = re.sub(r'(?im)^(nps|rand)\b.*\n?', '', source).rstrip('\n')
    return f'{source}\nnps 2000\nrand seed=12345\n'


def _run(directory, name, source):  # pragma: no cover (only with --run-mcnp)
    directory.mkdir()
    path = directory / f'{name}.inp'
    path.write_text(source)
    subprocess.run(['mcnp6', 'ixr', f'i={path.name}', f'n={name}.'], cwd=directory, capture_output=True, timeout=300, check=False)
    output = directory / f'{name}.o'
    return output.read_text(errors='replace') if output.exists() else ''


@pytest.mark.parametrize('path', INPS, ids=IDS)
class Test_Roundtrip_PyMCNP:
    def test_whole_file_is_parsed(self, path):
        _, remainder = pymcnp.Inp.from_file(path)

        assert remainder == ''

    def test_write_is_idempotent(self, path):
        inp, _ = pymcnp.Inp.from_file(path)
        written = inp.to_mcnp()

        again, _ = pymcnp.Inp.from_mcnp(written)

        assert again.to_mcnp() == written

    def test_lines_fit_in_80_columns(self, path):
        inp, _ = pymcnp.Inp.from_file(path)

        assert max(len(line) for line in inp.to_mcnp().splitlines()) <= 80


@pytest.mark.filterwarnings('ignore:Line exceeds 80 characters:pymcnp.abc.Warning')
@pytest.mark.parametrize('path', COMPLETE, ids=[f'{path.parent.name}/{path.stem}' for path in COMPLETE])
def test_written_file_reads_back_the_same(path):
    # What `to_mcnp` writes, wrapped at 80 columns, parses completely, to the same cards and values.
    inp, _ = pymcnp.Inp.from_file(path)

    again, remainder = pymcnp.Inp.from_mcnp(inp.to_mcnp())

    assert remainder == ''
    assert _canonical(again) == _canonical(inp)


def test_complete_fixtures_are_found():
    assert len(COMPLETE) >= 30


@pytest.mark.mcnp
@pytest.mark.skipif(shutil.which('mcnp6') is None, reason='mcnp6 is not installed')
@pytest.mark.parametrize('path', INPS, ids=IDS)
class Test_Roundtrip_MCNP:
    """
    Runs every example input through the real ``mcnp6``, as written and after a PyMCNP round trip.

    Opt-in, since each run takes up to minutes: ``python -m pytest --run-mcnp -m mcnp``.
    """

    def test_mcnp_accepts_original_and_rewritten(self, path, tmp_path):  # pragma: no cover (only with --run-mcnp)
        original = _fast(path.read_text())
        inp, _ = pymcnp.Inp.from_mcnp(original)
        rewritten = _fast(inp.to_mcnp())

        out_original = _run(tmp_path / 'original', path.stem, original)
        if not out_original:
            pytest.skip('mcnp6 on PATH does not produce output (stub or broken install)')
        assert 'fatal error' not in out_original

        out_rewritten = _run(tmp_path / 'rewritten', path.stem, rewritten)
        assert out_rewritten, 'MCNP did not run the rewritten input'
        assert 'fatal error' not in out_rewritten


def test_wrap_keeps_dollar_comment():
    source = 'title\n1 0 -1\n\n1 so 1\n\nimp:n 1 ' + ' '.join(['1'] * 60) + ' $ importance\n\n'
    inp, _ = pymcnp.Inp.from_mcnp(source)
    written = inp.to_mcnp()

    assert max(len(line) for line in written.splitlines()) <= 80
    assert '$ importance' in written
    again, _ = pymcnp.Inp.from_mcnp(written)
    assert again.to_mcnp() == written


def test_wrap_leaves_unsplittable_line():
    line = 'x' * 100

    assert _wrap(line) == line


LONG = 'a very long comment that goes on and on and on past the eighty column limit, yes'
BASE = 'title\n1 0 -1\n2 0 1\n\n1 so 1\n\n'


@pytest.mark.filterwarnings('ignore:Line exceeds 80 characters:pymcnp.abc.Warning')
@pytest.mark.parametrize('comment', [f'c {LONG}', f'  c {LONG}', f'    C {LONG}'])
def test_wrap_leaves_comment_cards(comment):
    # A comment card in columns 1-5 is never wrapped: its second half would become a continuation line.
    source = BASE + f'm1 13027 1\n{comment}\nnps 100\n'
    inp, _ = pymcnp.Inp.from_mcnp(source)

    written = inp.to_mcnp()

    assert written == source
    again, remainder = pymcnp.Inp.from_mcnp(written)
    assert remainder == ''
    assert _canonical(again) == _canonical(inp)


@pytest.mark.filterwarnings('ignore:Line exceeds 80 characters:pymcnp.abc.Warning')
@pytest.mark.parametrize('dollar', ['', ' $ the bins', '$ the bins'])
def test_wrap_keeps_continuation(dollar):
    # A long line that ends in `&` keeps it, so the line after it is still a continuation.
    source = BASE + 'si1 ' + ' '.join(str(i) for i in range(1, 30)) + f' &{dollar}\n30 31\nsp1 0 ' + ' '.join(['1'] * 31) + '\nnps 100\n'
    inp, _ = pymcnp.Inp.from_mcnp(source)

    written = inp.to_mcnp()

    assert max(len(line) for line in written.splitlines()) <= 80
    again, remainder = pymcnp.Inp.from_mcnp(written)
    assert remainder == ''
    assert _canonical(again) == _canonical(inp)
    assert len(again.data_cards()[0].i) == 31


@pytest.mark.filterwarnings('ignore:Line exceeds 80 characters:pymcnp.abc.Warning')
def test_wrap_keeps_indent_of_continuation():
    # valid_07 continues a cell card on a line indented by 5 spaces; wrapping that line keeps its indent, so it still
    # continues the card. (The f4 tally of valid_07 does not parse yet, so it is left out.)
    source = re.sub(r'(?m)^f4:p.*\n', '', (FILES / 'valid_07.inp').read_text())
    inp, remainder = pymcnp.Inp.from_mcnp(source)
    assert remainder == ''

    written = inp.to_mcnp()

    assert '\n     lat=1 fill=' in written
    again, remainder = pymcnp.Inp.from_mcnp(written)
    assert remainder == ''
    assert _canonical(again) == _canonical(inp)


@pytest.mark.parametrize('spaces, indent', [(1, 1), (4, 4), (5, 5), (17, 5), (76, 5)])
def test_wrap_indent(spaces, indent):
    # A wrapped line keeps an indent of 1-4 spaces, which starts a card in columns 2-5, and starts one indented by 5 or
    # more, a continuation line, at column 6, so a deeply indented line can still be shortened.
    lines = _wrap(' ' * spaces + ' '.join(['1.2345'] * 14)).split('\n')

    assert len(lines[0]) - len(lines[0].lstrip(' ')) == indent
    assert all(len(line) <= 80 for line in lines)
