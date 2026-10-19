import re
import pathlib

import pytest

import pymcnp
from .. import classes


class Test_Ptrac(classes.Test_Nonterminal):
    element = pymcnp.Ptrac
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac' / 'valid_38.ptrac').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]


FILES = pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac'


def _head(path: pathlib.Path, histories: int = 4) -> str:
    """Header and the first few histories, since parsing a whole 1 MB file is very slow."""

    text = path.read_text()
    starts = [match.start() for match in re.finditer(r'(?m)^ {10}\d+ +\d+$', text)]
    return text[: starts[histories]] if len(starts) > histories else text


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.ptrac')), ids=lambda path: path.name)
def test_valid_files_parse_completely(path: pathlib.Path) -> None:
    text = _head(path)
    ptrac, remainder = pymcnp.Ptrac.from_mcnp(text)
    assert remainder == ''
    assert ptrac.to_mcnp() == text


@pytest.mark.parametrize('path', sorted(FILES.glob('invalid*.ptrac')), ids=lambda path: path.name)
def test_invalid_files_are_rejected(path: pathlib.Path) -> None:
    try:
        _, remainder = pymcnp.Ptrac.from_mcnp(path.read_text())
        assert remainder
    except pymcnp.abc.Error:
        pass
