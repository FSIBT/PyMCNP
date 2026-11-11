import pymcnp
from ..... import classes


class Test_Energy(classes.Test_FromMcnp):
    element = pymcnp.meshtal.line.boundary.Energy
    EXAMPLES_FROM_MCNP_VALID = [
        '    Energy bin boundaries: 0.00E+00 1.00E+36',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
