import pymcnp
from .... import classes


class Test_ParenthesizedIntegers(classes.Test_Nonterminal):
    element = pymcnp.inp.group.ParenthesizedIntegers
    EXAMPLES_VALID = [
        '( 1 1 1 1 )',
        '(1 1 1)',
        '(1<1<2)',
        '(1<1 1[1 0 1:3]<2)',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
