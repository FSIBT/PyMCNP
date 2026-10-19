import pymcnp
from .... import classes


class Test_Xyzro(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Xyzro
    EXAMPLES_VALID = [
        '3.1 3.1 3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
