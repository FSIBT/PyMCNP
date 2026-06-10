import pymcnp
from ..... import classes


class Test_Rand(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Rand
    EXAMPLES_VALID = [
        'gen 1',
        'seed 1',
        'stride 1',
        'hist 1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
