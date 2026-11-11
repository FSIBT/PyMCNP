import pymcnp
from .... import classes


class Test_PhotonSample(classes.Test_FromMcnp):
    element = pymcnp.inp.group.PhotonSample
    EXAMPLES_FROM_MCNP_VALID = [
        '1 3.1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
