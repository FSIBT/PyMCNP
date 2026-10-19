import pymcnp
from ..... import classes


class Test_Fmult(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Fmult
    EXAMPLES_VALID = [
        'sfnu 3.1 3.1 3.1',
        'width 3.1',
        'sfyield 3.1',
        'watt 3.1 3.1',
        'method 1',
        'data 1',
        'shift 1',
    ]
    EXAMPLES_INVALID = [
        'data -1',
        'method -1',
        'shift -1',
        'hello',
    ]
