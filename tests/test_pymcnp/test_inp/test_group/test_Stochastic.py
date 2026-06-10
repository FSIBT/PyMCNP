import pymcnp
from .... import classes


class Test_Stochastic(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Stochastic
    EXAMPLES_VALID = [
        '1 3.1 3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
