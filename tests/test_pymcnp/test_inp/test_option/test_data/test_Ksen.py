import pymcnp
from ..... import classes


class Test_Ksen(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Ksen
    EXAMPLES_FROM_MCNP_VALID = [
        'iso 001001 001001 001001',
        'rxn 1 1 1',
        'mt 1 1 1',
        'erg 3.1 3.1 3.1',
        'ein 3.1 3.1 3.1',
        'legendre 1',
        'cos 3.1 3.1 3.1',
        'constrain yes',
        'cell 1 1 1 1',
        'mat 1 1 1 1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
