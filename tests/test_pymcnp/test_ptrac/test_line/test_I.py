import pymcnp
from .... import classes


class Test_I(classes.Test_Nonterminal):
    element = pymcnp.ptrac.line.I
    EXAMPLES_VALID = [
        '          1      1000',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
