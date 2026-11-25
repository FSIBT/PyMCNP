"""
Records the parse result of every fixture, so that changes to the parsers are detected.

The reference is ``files/snapshot.json``. Regenerate it only for an intended change of results:

    uv run python -c "import json,sys; sys.path.insert(0,'tests'); import snapshot; json.dump(snapshot.record_all(), open('files/snapshot.json','w'), indent=1, sort_keys=True)"
"""

import hashlib
import pathlib
import warnings

import pandas

import pymcnp

FILES: pathlib.Path = pathlib.Path(__file__).parent.parent / 'files'
SNAPSHOT: pathlib.Path = FILES / 'snapshot.json'

_CLASSES = {'inp': pymcnp.Inp, 'outp': pymcnp.Outp, 'meshtal': pymcnp.Meshtal, 'ptrac': pymcnp.Ptrac}


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


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
            result = {'ok': True, 'mcnp': _sha(obj.to_mcnp()), 'remainder': _sha(remainder), 'remainder_len': len(remainder)}
            if kind in ('outp', 'ptrac'):
                result['frame'] = _frame(obj.to_dataframe())
            elif kind == 'meshtal':
                frames = obj.to_dataframe()
                result['frame'] = [_frame(f) for f in (frames if isinstance(frames, list) else [frames])]
        except pymcnp.abc.Error as err:
            result = {'ok': False, 'error': str(err)}
        if kind == 'inp':
            result['problems'] = [[p.line, p.kind, p.message] for p in pymcnp.Check(path).problems()]
    return result


def fixtures() -> list[pathlib.Path]:
    return sorted(p for kind in _CLASSES for p in (FILES / kind).iterdir() if p.is_file())


def record_all() -> dict:
    return {str(p.relative_to(FILES)): record(p) for p in fixtures()}
