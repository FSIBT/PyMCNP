import pymcnp
from .... import classes


class Test_LatticeRange(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.LatticeRange
    EXAMPLES_VALID = [
        '1:1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
