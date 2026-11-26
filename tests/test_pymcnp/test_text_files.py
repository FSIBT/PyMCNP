"""
Tests that PyMCNP reads and writes text files the same way on every OS: any line end, UTF-8 whatever the locale.
"""

import os
import sys
import pathlib
import subprocess

import pytest

import pymcnp

FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files'


def _crlf(source: pathlib.Path, target: pathlib.Path) -> pathlib.Path:
    target.write_bytes(source.read_bytes().replace(b'\n', b'\r\n'))
    return target


def test_iter_histories_crlf(tmp_path: pathlib.Path) -> None:
    source = FILES / 'ptrac' / 'valid_38.ptrac'
    crlf = _crlf(source, tmp_path / 'crlf.ptrac')
    assert [h.to_mcnp() for h in pymcnp.Ptrac.iter_histories(crlf)] == [h.to_mcnp() for h in pymcnp.Ptrac.iter_histories(source)]


def test_iter_tallies_crlf(tmp_path: pathlib.Path) -> None:
    source = FILES / 'meshtal' / 'multi_00.meshtal'
    crlf = _crlf(source, tmp_path / 'crlf.meshtal')
    assert [t.to_mcnp() for t in pymcnp.Meshtal.iter_tallies(crlf)] == [t.to_mcnp() for t in pymcnp.Meshtal.iter_tallies(source)]


def test_inp_old_mac_line_ends(tmp_path: pathlib.Path) -> None:
    source = FILES / 'inp' / 'valid_00.inp'
    cr = tmp_path / 'cr.inp'
    cr.write_bytes(source.read_bytes().replace(b'\n', b'\r'))
    assert pymcnp.Inp.from_file(cr)[0].to_mcnp() == pymcnp.Inp.from_file(source)[0].to_mcnp()


def test_inp_utf8_byte_order_mark(tmp_path: pathlib.Path) -> None:
    # Windows Notepad can save UTF-8 with a byte order mark; it is not part of the title.
    source = FILES / 'inp' / 'valid_00.inp'
    bom = tmp_path / 'bom.inp'
    bom.write_bytes(b'\xef\xbb\xbf' + source.read_bytes())
    assert pymcnp.Inp.from_file(bom)[0].to_mcnp() == pymcnp.Inp.from_file(source)[0].to_mcnp()
    assert [p.line for p in pymcnp.Check(bom).problems()] == [p.line for p in pymcnp.Check(source).problems()]


# Runs in a child whose locale encoding is not UTF-8, as on Windows (cp1252).
# Its code is ASCII, which the command line of any locale can carry.
_CHILD = """
import sys, locale, pathlib, warnings
import pymcnp
print(locale.getencoding())
warnings.simplefilter('ignore')
files = pathlib.Path(sys.argv[1])
assert pymcnp.Ptrac.from_file(files / 'ptrac' / 'trailing_02.ptrac')[1] == '\\u3000'
assert pymcnp.Meshtal.from_file(files / 'meshtal' / 'trailing_07.meshtal')[1] == '\\u3000\\n'
text = (files / 'meshtal' / 'valid_41.meshtal').read_text(encoding='utf-8').replace('lunar regolith', 'Mondregolith \\u00e0 \\u03bb')
pathlib.Path('t.meshtal').write_bytes(text.encode('utf-8'))
assert '\\u03bb' in next(pymcnp.Meshtal.iter_tallies('t.meshtal')).title
text = (files / 'ptrac' / 'valid_38.ptrac').read_text(encoding='utf-8').replace('lunar regolith', 'lunar r\\u00e9golith')  # the title keeps its width
pathlib.Path('t.ptrac').write_bytes(text.encode('utf-8'))
assert len(list(pymcnp.Ptrac.iter_histories('t.ptrac'))) == len(list(pymcnp.Ptrac.iter_histories(files / 'ptrac' / 'valid_38.ptrac')))
inp = pymcnp.Inp.from_file(files / 'inp' / 'valid_00.inp')[0]
inp.title = 'Temperatur 20 \\u00b0C, \\u03bb = 1 \\u00c5\\n'
inp.to_file('out.inp')
assert pathlib.Path('out.inp').read_bytes().startswith('Temperatur 20 \\u00b0C, \\u03bb = 1 \\u00c5'.encode('utf-8'))
assert pymcnp.Inp.from_file('out.inp')[0].title == inp.title
assert not pymcnp.Check('out.inp').problems()
"""


def test_utf8_whatever_the_locale(tmp_path: pathlib.Path) -> None:
    env = dict(os.environ, PYTHONUTF8='0', PYTHONCOERCECLOCALE='0', LC_ALL='en_US.ISO8859-1' if sys.platform == 'darwin' else 'C')
    env.pop('PYTHONIOENCODING', None)
    done = subprocess.run([sys.executable, '-X', 'utf8=0', '-c', _CHILD, str(FILES)], cwd=tmp_path, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if done.stdout.partition('\n')[0].strip().replace('-', '').lower() == 'utf8':  # pragma: no cover (a platform with no other locale)
        pytest.skip(f'locale encoding is UTF-8 here: {done.stdout!r} {done.stderr[-300:]!r}')
    assert done.returncode == 0, done.stdout + done.stderr


# Readers, each with a fixture, a word of its free text (title or comment) and the line of that word.
READERS = [
    pytest.param(lambda path: pymcnp.Inp.from_file(path), 'inp/valid_00.inp', 'Problem', 1, id='Inp'),
    pytest.param(lambda path: pymcnp.Check(path).problems(), 'inp/valid_00.inp', 'Problem', 1, id='Check.problems'),
    pytest.param(lambda path: list(pymcnp.Check(path).check()), 'inp/valid_00.inp', 'Problem', 1, id='Check.check'),
    pytest.param(lambda path: pymcnp.Outp.from_file(path), 'outp/valid_39.outp', 'regolith', 39, id='Outp'),
    pytest.param(lambda path: pymcnp.Meshtal.from_file(path), 'meshtal/valid_41.meshtal', 'regolith', 2, id='Meshtal'),
    pytest.param(lambda path: list(pymcnp.Meshtal.iter_tallies(path)), 'meshtal/valid_41.meshtal', 'regolith', 2, id='Meshtal.iter_tallies'),
    pytest.param(lambda path: pymcnp.Ptrac.from_file(path), 'ptrac/valid_38.ptrac', 'regolith', 3, id='Ptrac'),
    pytest.param(lambda path: list(pymcnp.Ptrac.iter_histories(path)), 'ptrac/valid_38.ptrac', 'regolith', 3, id='Ptrac.iter_histories'),
    pytest.param(lambda path: list(pymcnp.Ptrac.stream(path)), 'ptrac/valid_38.ptrac', 'regolith', 3, id='Ptrac.stream'),
]


def _comparable(result) -> object:
    """
    Turns what a reader returns into something that compares by content.
    """

    if isinstance(result, (tuple, list)):
        return [_comparable(item) for item in result]
    if isinstance(result, pymcnp.abc.Symbol):
        return result.to_mcnp()
    return result


def _variant(fixture: str, word: str, target: pathlib.Path, encoding: str) -> pathlib.Path:
    # A non-ASCII letter replaces one of the word, so every line keeps its width.
    text = (FILES / fixture).read_text(encoding='utf-8')
    target.write_bytes(text.replace(word, word.replace('o', 'ö', 1).replace('e', 'é', 1), 1).encode(encoding))
    return target


@pytest.mark.filterwarnings('ignore:Tally not parsed:pymcnp.abc.Warning')
@pytest.mark.parametrize('read, fixture, word, line', READERS)
def test_latin_1_file_reads_with_a_warning(tmp_path: pathlib.Path, read, fixture: str, word: str, line: int) -> None:
    # A file saved as Latin-1 or cp1252, e.g., by a Windows editor, reads as Latin-1, with a warning naming its first
    # line that is not UTF-8, as a UTF-8 file with the same text reads.
    utf8 = _variant(fixture, word, tmp_path / 'utf8', 'utf-8')
    latin1 = _variant(fixture, word, tmp_path / 'latin1', 'cp1252')

    with pytest.warns(pymcnp.abc.Warning, match=rf'not UTF-8[\s\S]*latin1, line {line}$') as records:
        result = read(latin1)
    assert len([record for record in records if 'UTF-8' in str(record.message)]) == 1
    assert _comparable(result) == _comparable(read(utf8))


@pytest.mark.parametrize('read, fixture, word, line', READERS)
def test_binary_file_raises(tmp_path: pathlib.Path, read, fixture: str, word: str, line: int) -> None:
    # A NUL byte, which no text file holds, e.g., a PTRAC file MCNP wrote in binary, its default.
    binary = tmp_path / 'binary'
    binary.write_bytes((FILES / fixture).read_bytes()[:500] + b'\x00\x00\x01\xff')

    with pytest.raises(UnicodeDecodeError, match='NUL byte') as info:
        read(binary)
    assert info.value.start == 500


def test_encoding_found_over_chunk_boundaries(tmp_path: pathlib.Path, monkeypatch) -> None:
    # The file is checked in chunks: a character cut by a chunk boundary is UTF-8, and lines are counted across chunks.
    from pymcnp.abc import _text

    monkeypatch.setattr(_text, '_CHUNK', 7)
    path = tmp_path / 'text'
    path.write_bytes('aéééééééé long line without a newline\nb\né\n'.encode('utf-8'))
    assert _text.read_text(path) == 'aéééééééé long line without a newline\nb\né\n'
    path.write_bytes('aé\nbbbbbbbbbbbbbbbbbbb\nc\né'.encode('utf-8') + b'\n\xe9\nd')
    with pytest.warns(pymcnp.abc.Warning, match=r'text, line 5$'):
        assert _text.read_text(path) == 'aÃ©\nbbbbbbbbbbbbbbbbbbb\nc\nÃ©\né\nd'
    path.write_bytes(b'a\nbbbbbbbbbbbbbbbbbbb\nc\x00')
    with pytest.raises(UnicodeDecodeError, match='NUL byte') as info:
        _text.read_text(path)
    assert info.value.start == 23


def test_latin_1_line_ends(tmp_path: pathlib.Path) -> None:
    # Latin-1 text with Windows line ends reads with LF line ends, as UTF-8 text does.
    path = tmp_path / 'crlf'
    path.write_bytes(b'\xe9\r\nb\r\n')
    with pytest.warns(pymcnp.abc.Warning, match='line 1$'):
        from pymcnp.abc import _text

        assert _text.read_text(path) == 'é\nb\n'
        with _text.open_text(path) as file:
            assert file.read() == 'é\nb\n'
