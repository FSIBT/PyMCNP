import pymcnp
from .... import classes


class Test_EmbeddedDistribution(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.EmbeddedDistribution
    EXAMPLES_VALID = ['D1<D2<D3']
    EXAMPLES_INVALID = [
        'hello',
    ]
