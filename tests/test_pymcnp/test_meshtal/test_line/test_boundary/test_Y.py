import pymcnp
from ..... import classes


class Test_Y(classes.Test_Nonterminal):
    element = pymcnp.meshtal.line.boundary.Y
    EXAMPLES_VALID = [
        '    Y direction:   -100.00    -80.00    -60.00    -40.00    -20.00      0.00     20.00     40.00     60.00     80.00    100.00',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
