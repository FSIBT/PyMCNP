import pymcnp
from .... import classes


class Test_Jump(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Jump
    EXAMPLES_VALID = [
        'J',
        'j',
    ]
    EXAMPLES_INVALID = ['hello', '2j']
