import pymcnp
from .... import classes


class Test_Tally(classes.Test_FromMcnp):
    element = pymcnp.outp.line.Tally
    EXAMPLES_FROM_MCNP_VALID = [
        '    0.0000E+00   0.00000E+00 0.0000',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
