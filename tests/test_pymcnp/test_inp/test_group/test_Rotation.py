import pymcnp
from .... import classes


class Test_Rotation(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Rotation
    EXAMPLES_VALID = [
        '3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 1',
        '3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1',
        '3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 1',
        '3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1',
        '3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 1',
        '3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1',
        '3.1 3.1 3.1 3.1 3.1 3.1 1',
        '3.1 3.1 3.1 3.1 3.1 3.1',
        '3.1 3.1 3.1 1',
        '3.1 3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
