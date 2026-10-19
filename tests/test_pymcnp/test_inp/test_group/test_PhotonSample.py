import pymcnp
from .... import classes


class Test_PhotonSample(classes.Test_Nonterminal):
    element = pymcnp.inp.group.PhotonSample
    EXAMPLES_VALID = [
        '1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
