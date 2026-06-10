import pymcnp
from ..... import classes


class Test_Time(classes.Test_Nonterminal):
    element = pymcnp.meshtal.line.boundary.Time
    EXAMPLES_VALID = ['    Time bin boundaries:  -1.00E+36 2.00E+00 3.00E+00 4.00E+00 1.00E+03']
    EXAMPLES_INVALID = [
        'hello',
    ]
