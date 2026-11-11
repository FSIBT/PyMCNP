import pymcnp
from ..... import classes


class Test_Rand(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Rand
    EXAMPLES_FROM_MCNP_VALID = [
        'gen 1',
        'seed 1',
        'stride 1',
        'hist 1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
