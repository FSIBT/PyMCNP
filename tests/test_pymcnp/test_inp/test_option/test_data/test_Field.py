import pymcnp
from ..... import classes


class Test_Field(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Field
    EXAMPLES_FROM_MCNP_VALID = [
        'gcut 3.1',
        'gpar 3.1',
        'grad 3.1',
        'gsur 1 1 1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
