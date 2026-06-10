import pymcnp
from ..... import classes


class Test_Var(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Var
    EXAMPLES_VALID = [
        'rr off',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
