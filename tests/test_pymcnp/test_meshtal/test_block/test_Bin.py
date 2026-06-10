import pymcnp
from .... import classes


class Test_Bin(classes.Test_Nonterminal):
    element = pymcnp.meshtal.block.Bin
    EXAMPLES_VALID = [
        ' Tally bin boundaries:\n    X direction:   -100.00    -50.00      0.00     50.00    100.00\n    Y direction:   -100.00    -50.00      0.00     50.00    100.00\n    Z direction:   -150.00   -125.00   -100.00    -75.00    -50.00\n    Time bin boundaries:  -1.00E+36 2.00E+00 3.00E+00\n    Energy bin boundaries: 0.00E+00 3.00E+00 1.40E+01',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
