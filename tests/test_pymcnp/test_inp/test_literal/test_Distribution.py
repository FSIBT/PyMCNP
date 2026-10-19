import pymcnp
from .... import classes


class Test_Distribution(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Distribution
    EXAMPLES_VALID = ['D1']
    EXAMPLES_INVALID = [
        'hello',
    ]
