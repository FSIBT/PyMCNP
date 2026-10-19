import pymcnp
from .... import classes


class Test_N(classes.Test_Nonterminal):
    element = pymcnp.ptrac.line.N
    EXAMPLES_VALID = [
        '     2    5    3    6    3    6    3    6    3    6    3    1    4    0    0    0    0    0    0    0',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
