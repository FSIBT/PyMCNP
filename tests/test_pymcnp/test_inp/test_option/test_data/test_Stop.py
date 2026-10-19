import pymcnp
from ..... import classes


class Test_Stop(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Stop
    EXAMPLES_VALID = [
        'nps 1 1',
        'ctme 3.1',
        'f1 1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
