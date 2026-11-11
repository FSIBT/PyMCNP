import pymcnp
from .... import classes


class Test_PhotonBias(classes.Test_FromMcnp):
    element = pymcnp.inp.group.PhotonBias
    EXAMPLES_FROM_MCNP_VALID = [
        '001001 1',
        '001001 1 1 3.1 1 3.1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
