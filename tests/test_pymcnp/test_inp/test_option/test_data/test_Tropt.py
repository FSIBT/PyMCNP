import pymcnp
from ..... import classes


class Test_Tropt(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Tropt
    EXAMPLES_FROM_MCNP_VALID = [
        'mcscat off',
        'eloss off',
        'nreact off',
        'nescat off',
        'genxs hello',
        'genxs',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
