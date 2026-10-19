import pymcnp
from ..... import classes


class Test_T(classes.Test_Nonterminal):
    element = pymcnp.inp.card.data.T
    EXAMPLES_VALID = [
        't4 0 10 100',
        't4 0 10 100 nt',
        't0 0 10 100 c',
        't14 cbeg=0 csub=2',
    ]
    EXAMPLES_INVALID = [
        't100000000 0 10',
    ]
