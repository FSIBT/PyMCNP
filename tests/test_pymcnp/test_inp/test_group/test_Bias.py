import pymcnp
from .... import classes


class Test_Bias(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Bias
    EXAMPLES_VALID = [
        '3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
