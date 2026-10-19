import pymcnp
from .... import classes


class Test_Location(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Location
    EXAMPLES_VALID = ['3.1 3.1 3.1']
    EXAMPLES_INVALID = [
        'hello',
    ]
