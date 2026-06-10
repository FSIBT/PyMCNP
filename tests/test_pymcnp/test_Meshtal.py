import pathlib

import pymcnp
from .. import classes


class Test_Meshtal(classes.Test_Nonterminal):
    element = pymcnp.Meshtal
    EXAMPLES_VALID = [(pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal' / 'valid_40.meshtal').read_text()]
    EXAMPLES_INVALID = [
        'hello',
    ]
