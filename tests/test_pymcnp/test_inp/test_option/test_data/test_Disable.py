import pymcnp
from ..... import classes


class Test_Disable(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Disable
    EXAMPLES_FROM_MCNP_VALID = [
        'nuclide_activity_table',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
