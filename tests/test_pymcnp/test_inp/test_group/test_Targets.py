import pymcnp
from .... import classes


class Test_Targets(classes.Test_FromMcnp):
    element = pymcnp.inp.group.Targets
    EXAMPLES_FROM_MCNP_VALID = [
        '001001 001001',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
