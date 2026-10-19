import pymcnp
from ..... import classes


class Test_Embee(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Embee
    EXAMPLES_VALID = [
        'embed 1',
        'comment hello',
        'energy 3.1',
        'errors yes',
        'time 3.1',
        'atom yes',
        'factor 3.1',
        'list 3.1',
        'mat 1',
        'mtype flux',
    ]
    EXAMPLES_INVALID = [
        'mat -1',
        'hello',
    ]
