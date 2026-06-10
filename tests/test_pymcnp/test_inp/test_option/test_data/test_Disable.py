import pymcnp
from ..... import classes


class Test_Disable(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Disable
    EXAMPLES_VALID = [
        'nuclide_activity_table',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
