import pymcnp
from ..... import classes


class Test_C(classes.Test_FromMcnp):
    element = pymcnp.inp.card.data.C
    EXAMPLES_FROM_MCNP_VALID = [
        'c1 -0.5 0 1',
        'c1 0 1',
        '*c1 90 0',
        '*c21 179 90 0',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'c1 -2 1',
        'c1 0 0.5',
        '*c1 90 10',
        '*c1 200 0',
    ]
