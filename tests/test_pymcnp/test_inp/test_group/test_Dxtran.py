import pymcnp
from .... import classes


class Test_Dxtran(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Dxtran
    EXAMPLES_VALID = [
        '3.1 3.1 3.1 3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
