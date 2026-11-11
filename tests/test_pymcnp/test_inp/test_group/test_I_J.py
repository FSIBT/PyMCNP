import pymcnp
from .... import classes


class Test_I_J(classes.Test_FromMcnp):
    element = pymcnp.inp.group.I_J
    EXAMPLES_FROM_MCNP_VALID = [
        '1 3.1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
