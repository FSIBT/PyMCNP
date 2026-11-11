import pymcnp
from .... import classes


class Test_Location(classes.Test_FromMcnp):
    element = pymcnp.inp.group.Location
    EXAMPLES_FROM_MCNP_VALID = ['3.1 3.1 3.1']
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
