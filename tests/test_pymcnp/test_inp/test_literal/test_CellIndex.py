import pymcnp
from .... import classes


class Test_CellIndex(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.CellIndex
    EXAMPLES_VALID = ['D1<1[1 0 3]<1 3 5[0 3 3:3]<1 4 5']
    EXAMPLES_INVALID = [
        'hello',
    ]
