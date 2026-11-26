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
_CHILD = """
import sys, locale, pathlib, warnings
import pymcnp
print(locale.getencoding())
warnings.simplefilter('ignore')
files = pathlib.Path(sys.argv[1])
assert pymcnp.Ptrac.from_file(files / 'ptrac' / 'trailing_02.ptrac')[1] == '\\u3000'
assert pymcnp.Meshtal.from_file(files / 'meshtal' / 'trailing_07.meshtal')[1] == '\\u3000\\n'
text = (files / 'meshtal' / 'valid_41.meshtal').read_text(encoding='utf-8').replace('lunar regolith', 'Mondregolith \u00e0 \u03bb')
pathlib.Path('t.meshtal').write_bytes(text.encode('utf-8'))
assert '\u03bb' in next(pymcnp.Meshtal.iter_tallies('t.meshtal')).title
text = (files / 'ptrac' / 'valid_38.ptrac').read_text(encoding='utf-8').replace('lunar regolith', 'lunar r\u00e9golith')  # the title keeps its width
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
