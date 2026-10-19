import pymcnp
from .... import classes


class Test_Constituent(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Constituent
    EXAMPLES_VALID = [
        '001001 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
