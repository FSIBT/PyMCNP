import pymcnp
from .... import classes


class Test_Aorro(classes.Test_FromMcnp):
    element = pymcnp.inp.group.Aorro
    EXAMPLES_FROM_MCNP_VALID = ['3.1 3.1 3.1']
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
