import pymcnp
from ..... import classes


class Test_Var(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Var
    EXAMPLES_FROM_MCNP_VALID = [
        'rr off',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
