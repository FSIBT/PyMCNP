import pymcnp
from ..... import classes


class Test_Dawwg(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Dawwg
    EXAMPLES_FROM_MCNP_VALID = [
        'points 1',
        'xsec hello',
        'block 1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
