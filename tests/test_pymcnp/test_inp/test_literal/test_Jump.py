import pymcnp
from .... import classes


class Test_Jump(classes.Test_FromMcnp):
    element = pymcnp.inp.literal.Jump
    EXAMPLES_FROM_MCNP_VALID = [
        'J',
        'j',
    ]
    EXAMPLES_FROM_MCNP_INVALID = ['hello', '2j']
