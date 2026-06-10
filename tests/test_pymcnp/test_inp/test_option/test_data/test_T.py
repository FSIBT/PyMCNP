import pymcnp
from ..... import classes


class Test_T(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.T
    EXAMPLES_VALID = [
        'cbeg 3.1',
        'cfrq 3.1',
        'cofi 3.1',
        'coni 3.1',
        'csub 1',
        'cend 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
