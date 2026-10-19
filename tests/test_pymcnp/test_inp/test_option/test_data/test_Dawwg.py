import pymcnp
from ..... import classes


class Test_Dawwg(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Dawwg
    EXAMPLES_VALID = [
        'points 1',
        'xsec hello',
        'block 1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
