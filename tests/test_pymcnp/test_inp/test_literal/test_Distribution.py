import pymcnp
from .... import classes


class Test_Distribution(classes.Test_FromMcnp):
    element = pymcnp.inp.literal.Distribution
    EXAMPLES_FROM_MCNP_VALID = ['D1']
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
