import pathlib

import pymcnp
from .. import classes


class Test_Outp(classes.Test_Nonterminal):
    element = pymcnp.Outp
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_39.outp').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]


def test_fatal_errors() -> None:
    from pymcnp.Outp import _fatal_errors

    text = '  comment.  fine\n  fatal error.  surface        -7 not found for cell         2 card.\n \n  fatal error.  surface -7 of cell 2 is not defined.\n  warning.  nothing\n'
    assert _fatal_errors(text) == ['surface        -7 not found for cell         2 card.', 'surface -7 of cell 2 is not defined.']
    assert _fatal_errors('  warning.  no fatal error here\n') == []
