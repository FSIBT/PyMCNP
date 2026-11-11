import pymcnp
from .... import classes


class Test_Stochastic(classes.Test_FromMcnp):
    element = pymcnp.inp.group.Stochastic
    EXAMPLES_FROM_MCNP_VALID = [
        '1 3.1 3.1 3.1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
