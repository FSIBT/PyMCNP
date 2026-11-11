import pymcnp
from .... import classes


class Test_V_S(classes.Test_FromMcnp):
    element = pymcnp.inp.group.V_S
    EXAMPLES_FROM_MCNP_VALID = [
        '1 D1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
