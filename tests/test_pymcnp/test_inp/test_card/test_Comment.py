import pymcnp
from .... import classes


class Test_Comment(classes.Test_Nonterminal):
    element = pymcnp.inp.card.Comment
    EXAMPLES_VALID = [
        'c',
        'c Hello!',
        '  c Hello!',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
