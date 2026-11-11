import pymcnp
from .... import classes


class Test_Constituent(classes.Test_FromMcnp):
    element = pymcnp.inp.group.Constituent
    EXAMPLES_FROM_MCNP_VALID = [
        '001001 3.1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
