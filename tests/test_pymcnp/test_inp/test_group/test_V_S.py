import pymcnp
from .... import classes


class Test_V_S(classes.Test_Nonterminal):
    element = pymcnp.inp.group.V_S
    EXAMPLES_VALID = [
        '1 D1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
