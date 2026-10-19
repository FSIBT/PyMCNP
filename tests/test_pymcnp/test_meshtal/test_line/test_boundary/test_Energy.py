import pymcnp
from ..... import classes


class Test_Energy(classes.Test_Nonterminal):
    element = pymcnp.meshtal.line.boundary.Energy
    EXAMPLES_VALID = [
        '    Energy bin boundaries: 0.00E+00 1.00E+36',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
