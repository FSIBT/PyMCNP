import pymcnp
from ..... import classes


class Test_Stop(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Stop
    EXAMPLES_FROM_MCNP_VALID = [
        'nps 1 1',
        'ctme 3.1',
        'f1 1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
