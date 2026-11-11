import pymcnp
from ..... import classes


class Test_X(classes.Test_FromMcnp):
    element = pymcnp.meshtal.line.boundary.X
    EXAMPLES_FROM_MCNP_VALID = [
        '    X direction:   -100.00    -80.00    -60.00    -40.00    -20.00      0.00     20.00     40.00     60.00     80.00    100.00',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
