import pymcnp
from ..... import classes


class Test_Read(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Read
    EXAMPLES_FROM_MCNP_VALID = [
        'decode hello',
        'echo',
        'encode hello',
        'file hello',
        'noecho',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
