import pymcnp
from ..... import classes


class Test_Tropt(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Tropt
    EXAMPLES_VALID = [
        'mcscat off',
        'eloss off',
        'nreact off',
        'nescat off',
        'genxs hello',
        'genxs',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
