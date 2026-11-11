import pymcnp
from .... import classes


class Test_MatCell(classes.Test_FromMcnp):
    element = pymcnp.inp.group.MatCell
    EXAMPLES_FROM_MCNP_VALID = [
        '1 1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
