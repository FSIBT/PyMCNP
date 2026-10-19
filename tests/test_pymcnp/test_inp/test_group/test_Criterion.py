import pymcnp
from .... import classes


class Test_Criterion(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Criterion
    EXAMPLES_VALID = [
        '3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
