import pymcnp
from .... import classes


class Test_P(classes.Test_Nonterminal):
    element = pymcnp.ptrac.line.P
    EXAMPLES_VALID = [
        '  -0.54320E+01  0.76877E+01 -0.52135E+00',
        '  -0.54320E+01  0.76877E+01 -0.52135E+00 -0.54320E+01  0.76877E+01 -0.52135E+00 -0.54320E+01  0.76877E+01 -0.52135E+00',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
