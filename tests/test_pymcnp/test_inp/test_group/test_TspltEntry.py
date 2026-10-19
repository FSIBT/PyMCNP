import pymcnp
from .... import classes


class Test_TspltEntry(classes.Test_Nonterminal):
    element = pymcnp.inp.group.TspltEntry
    EXAMPLES_VALID = [
        '3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
