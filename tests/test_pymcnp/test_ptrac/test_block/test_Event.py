import pymcnp
from .... import classes


class Test_Event(classes.Test_Nonterminal):
    element = pymcnp.ptrac.block.Event
    EXAMPLES_VALID = [
        '       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
