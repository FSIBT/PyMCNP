import pymcnp
from .... import classes


class Test_Targets(classes.Test_Nonterminal):
    element = pymcnp.inp.group.Targets
    EXAMPLES_VALID = [
        '001001 001001',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
