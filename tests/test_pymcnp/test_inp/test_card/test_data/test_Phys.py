import pymcnp
from ..... import classes


class Test_Phys_4(classes.Test_Nonterminal):
    element = pymcnp.inp.card.data.Phys_4
    EXAMPLES_INVALID = [
        'phys:h J J J J J J J J J J J J J J J J J',
    ]
