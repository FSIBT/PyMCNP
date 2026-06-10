import pymcnp
from ..... import classes


class Test_Read(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Read
    EXAMPLES_VALID = [
        'decode hello',
        'echo',
        'encode hello',
        'file hello',
        'noecho',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
