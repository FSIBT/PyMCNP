import pathlib

import pytest

import pymcnp
from .. import classes


class Test_Meshtal(classes.Test_Nonterminal):
    element = pymcnp.Meshtal
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal' / 'valid_40.meshtal').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]


FILES = pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal'


@pytest.mark.parametrize('path', sorted(FILES.glob('valid*.meshtal')), ids=lambda path: path.name)
def test_valid_files_parse_completely(path: pathlib.Path) -> None:
    text = path.read_text()
    meshtal, remainder = pymcnp.Meshtal.from_mcnp(text)
    assert remainder == ''
    assert meshtal.to_mcnp() == text


@pytest.mark.parametrize('path', sorted(FILES.glob('invalid*.meshtal')), ids=lambda path: path.name)
def test_invalid_files_are_rejected(path: pathlib.Path) -> None:
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.Meshtal.from_mcnp(path.read_text())
