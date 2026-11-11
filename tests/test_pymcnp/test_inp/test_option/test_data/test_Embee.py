import pymcnp
from ..... import classes


class Test_Embee(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Embee
    EXAMPLES_FROM_MCNP_VALID = [
        'embed 1',
        'comment hello',
        'energy 3.1',
        'errors yes',
        'time 3.1',
        'atom yes',
        'factor 3.1',
        'list 3.1',
        'mat 1',
        'mtype flux',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'mat -1',
        'hello',
    ]
