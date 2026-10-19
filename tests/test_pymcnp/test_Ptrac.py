import pathlib

import pymcnp
from .. import classes


class Test_Ptrac(classes.Test_Nonterminal):
    element = pymcnp.Ptrac
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac' / 'valid_38.ptrac').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]
