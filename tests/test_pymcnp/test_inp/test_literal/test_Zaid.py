import pymcnp
from .... import classes


class Test_Zaid(classes.Test_FromMcnp):
    element = pymcnp.inp.literal.Zaid
    EXAMPLES_FROM_MCNP_VALID = [
        '001001',
        'hello',
        'h-zr.20t',
        'h/zr.28t',
        'lwtr.23t',
    ]
    EXAMPLES_FROM_MCNP_REMAINDER = {
        '001001.hi': '.hi',
    }
