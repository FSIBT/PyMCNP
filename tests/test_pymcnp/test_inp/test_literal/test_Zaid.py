import pymcnp
from .... import classes


class Test_Zaid(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Zaid
    EXAMPLES_VALID = [
        '001001',
        'hello',
        'h-zr.20t',
        'h/zr.28t',
        'lwtr.23t',
    ]
    EXAMPLES_INVALID = [
        '001001.hi',
    ]
