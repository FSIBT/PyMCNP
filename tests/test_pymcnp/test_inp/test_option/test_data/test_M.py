import pymcnp
from ..... import classes


class Test_M(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.M
    EXAMPLES_VALID = [
        'gas 0',
        'estep 1',
        'hstep 1',
        'nlib hello',
        'plib hello',
        'pnlib hello',
        'elib hello',
        'hlib hello',
        'alib hello',
        'slib hello',
        'tlib hello',
        'dlib hello',
        'cond 3.1',
        'refi 3.1',
        'refc 3.1 3.1 3.1 3.1',
        'refs 3.1 3.1 3.1 3.1 3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
