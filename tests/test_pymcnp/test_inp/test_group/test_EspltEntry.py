import pymcnp
from .... import classes


class Test_EspltEntry(classes.Test_Nonterminal):
    element = pymcnp.inp.group.EspltEntry
    EXAMPLES_VALID = [
        '3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
