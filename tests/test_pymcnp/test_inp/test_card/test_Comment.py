import pymcnp
from .... import classes


class Test_Comment(classes.Test_FromMcnp):
    element = pymcnp.inp.card.Comment
    EXAMPLES_FROM_MCNP_VALID = [
        'c',
        'c Hello!',
        '  c Hello!',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
