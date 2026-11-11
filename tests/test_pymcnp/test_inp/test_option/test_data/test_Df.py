import pymcnp
from ..... import classes


class Test_Df(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Df
    EXAMPLES_FROM_MCNP_VALID = [
        'iu 1',
        'fac 1',
        'ic 99',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'iu=30',
        'fac=-102',
        'ic=1',
        'hello',
    ]
