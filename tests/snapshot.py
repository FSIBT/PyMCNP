"""
Records the parse result of every fixture, so that changes to the parsers are detected.

The reference is ``files/snapshot.json``. Regenerate it only for an intended change of results:

    uv run python -c "import json,sys; sys.path.insert(0,'tests'); import snapshot; json.dump(snapshot.record_all(), open('files/snapshot.json','w'), indent=1, sort_keys=True)"
"""

import hashlib
import pathlib
import re
import warnings

import pandas

import pymcnp

FILES: pathlib.Path = pathlib.Path(__file__).parent.parent / 'files'
SNAPSHOT: pathlib.Path = FILES / 'snapshot.json'

_CLASSES = {'inp': pymcnp.Inp, 'outp': pymcnp.Outp, 'meshtal': pymcnp.Meshtal, 'ptrac': pymcnp.Ptrac}


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


_FLOAT = re.compile(r'(?<![\w.])[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?(?![\w.])')


def _norm(text: str) -> str:
    """
    Rounds every standalone float literal to 12 significant digits.

    PyMCNP expands shorthand such as ``100log`` or ``8i`` into floats whose last digits come from
    the platform's libm, so they differ between macOS and glibc. Integers, identifiers and tokens
    such as ``92235.80c`` (not a whole float) are left untouched.
    """

    def fix(m: re.Match) -> str:
        tok = m.group()
        return format(float(tok), '.12g') if re.search(r'[.eE]', tok) else tok

    return _FLOAT.sub(fix, text)


def _frame(df: pandas.DataFrame) -> dict:
    """
    Fingerprints a dataframe by its CSV text, which is stable across pandas versions.
    """

    return {'columns': [str(c) for c in df.columns], 'dtypes': [str(t) for t in df.dtypes], 'hash': _sha(df.to_csv(index=True))}


def record(path: pathlib.Path) -> dict:
    """
    Records the parse result of the fixture at ``path``.
    """

    kind = path.parent.name
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        result: dict
        try:
            obj, remainder = _CLASSES[kind].from_file(path)
            result = {'ok': True, 'mcnp': _sha(_norm(obj.to_mcnp())), 'remainder': _sha(_norm(remainder)), 'remainder_len': len(remainder)}
            if kind in ('outp', 'ptrac'):
                result['frame'] = _frame(obj.to_dataframe())
            elif kind == 'meshtal':
                result['frame'] = [_frame(obj.to_dataframe())]  # a list, as recorded
        except pymcnp.abc.Error as err:
            result = {'ok': False, 'error': str(err)}
        if kind == 'inp':
            result['problems'] = [[p.line, p.kind, p.message] for p in pymcnp.Check(path).problems()]
    return result


def fixtures() -> list[pathlib.Path]:
    return sorted(p for kind in _CLASSES for p in (FILES / kind).iterdir() if p.is_file())


def record_all() -> dict:
    return {str(p.relative_to(FILES)): record(p) for p in fixtures()}
