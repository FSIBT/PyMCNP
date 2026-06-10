import pymcnp
from .... import classes


class Test_MatCell(classes.Test_Nonterminal):
    element = pymcnp.inp.group.MatCell
    EXAMPLES_VALID = [
        '1 1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
