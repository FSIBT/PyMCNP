import pymcnp
from .... import classes


class Test_Particle(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Particle
    EXAMPLES_VALID = [
        '@,#',
        '_',
        '#',
        'n',
        'P,n',
        'P,e,!',
    ]
    EXAMPLES_INVALID = [
        ':',
    ]
