import pymcnp
from .... import classes


class Test_LatticeRange(classes.Test_FromMcnp):
    element = pymcnp.inp.literal.LatticeRange
    EXAMPLES_FROM_MCNP_VALID = [
        '1:1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
