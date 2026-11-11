import pymcnp
from .... import classes


class Test_Qvm(classes.Test_FromMcnp):
    element = pymcnp.inp.literal.Qvm
    EXAMPLES_FROM_MCNP_VALID = [
        '+3.1v1',
        '-3.1v1',
        '3.1v1',
        '3.1X',
        '3.1Y',
        '3.1Z',
        '0',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
