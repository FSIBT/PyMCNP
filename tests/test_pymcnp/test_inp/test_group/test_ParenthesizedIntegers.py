import pymcnp
from .... import classes


class Test_ParenthesizedIntegers(classes.Test_FromMcnp):
    element = pymcnp.inp.group.ParenthesizedIntegers
    EXAMPLES_FROM_MCNP_VALID = [
        '( 1 1 1 1 )',
        '(1 1 1)',
        '(1<1<2)',
        '(1<1 1[1 0 1:3]<2)',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
