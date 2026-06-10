import pymcnp
from .... import classes


class Test_J(classes.Test_Nonterminal):
    element = pymcnp.ptrac.line.J
    EXAMPLES_VALID = [
        '       3000         1        40        15         2',
        '       3000         1        40         2         1         1',
        '       3000         1        40         2         1         1         1',
        '       3000         1        40         2         1         1         1         1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
