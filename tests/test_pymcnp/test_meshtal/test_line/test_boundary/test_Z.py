import pymcnp
from ..... import classes


class Test_Z(classes.Test_FromMcnp):
    element = pymcnp.meshtal.line.boundary.Z
    EXAMPLES_FROM_MCNP_VALID = [
        '    Z direction:   -100.00    -80.00    -60.00    -40.00    -20.00      0.00     20.00     40.00     60.00     80.00    100.00',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
