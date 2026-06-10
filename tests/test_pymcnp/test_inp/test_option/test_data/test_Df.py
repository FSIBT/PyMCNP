import pymcnp
from ..... import classes


class Test_Df(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Df
    EXAMPLES_VALID = [
        'iu 1',
        'fac 1',
        'ic 99',
    ]
    EXAMPLES_INVALID = [
        'iu=30',
        'fac=-102',
        'ic=1',
        'hello',
    ]
