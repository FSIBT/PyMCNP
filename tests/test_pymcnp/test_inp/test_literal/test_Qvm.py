import pymcnp
from .... import classes


class Test_Qvm(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Qvm
    EXAMPLES_VALID = [
        '+3.1v1',
        '-3.1v1',
        '3.1v1',
        '3.1X',
        '3.1Y',
        '3.1Z',
        '0',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
