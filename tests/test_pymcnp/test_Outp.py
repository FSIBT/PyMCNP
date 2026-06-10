import pathlib

import pymcnp
from .. import classes


class Test_Outp(classes.Test_Nonterminal):
    element = pymcnp.Outp
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_39.outp').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]
