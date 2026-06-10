import pymcnp
from .... import classes


class Test_Aorro(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Aorro
    EXAMPLES_VALID = ['3.1 3.1 3.1']
    EXAMPLES_INVALID = [
        'hello',
    ]
