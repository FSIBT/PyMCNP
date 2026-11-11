import pymcnp
from ..... import classes


class Test_Burn(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Burn
    EXAMPLES_FROM_MCNP_VALID = [
        'afmin 3.1 3.1',
        'bopt 3.1 3.1 1',
        'mat 1 1 1 1',
        'matvol 3.1',
        'nostats',
        'pfrac 3.1 3.1 3.1 3.1',
        'power 3.1',
        'time 3.1 3.1 3.1 3.1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'bopt 3.1 3.1 2',
        'hello',
    ]
