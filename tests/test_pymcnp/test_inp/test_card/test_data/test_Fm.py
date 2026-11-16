import pymcnp
from ..... import classes


class Test_Fm(classes.Test_FromMcnp):
    element = pymcnp.inp.card.data.Fm

    EXAMPLES_FROM_MCNP_INVALID = [
        'fm-1 -1 20 102 $ Na-24 production (not in material 11)',
    ]
