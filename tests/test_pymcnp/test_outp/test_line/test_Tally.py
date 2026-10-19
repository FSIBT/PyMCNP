import pymcnp
from .... import classes


class Test_Tally(classes.Test_Nonterminal):
    element = pymcnp.outp.line.Tally
    EXAMPLES_VALID = [
        '    0.0000E+00   0.00000E+00 0.0000',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
