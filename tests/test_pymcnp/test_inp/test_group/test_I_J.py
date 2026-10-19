import pymcnp
from .... import classes


class Test_I_J(classes.Test_Nonterminal):
    element = pymcnp.inp.group.I_J
    EXAMPLES_VALID = [
        '1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
