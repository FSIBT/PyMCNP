import pymcnp
from .... import classes


class Test_Zaid(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Zaid
    EXAMPLES_VALID = [
        '001001',
        'hello',
    ]
    EXAMPLES_INVALID = [
        '001001.hi',
    ]
