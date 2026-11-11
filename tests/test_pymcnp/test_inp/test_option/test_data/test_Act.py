import pymcnp
from ..... import classes


class Test_Act(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Act
    EXAMPLES_FROM_MCNP_VALID = [
        'fission none',
        'nonfiss none',
        'dn model',
        'dg none',
        'thresh 0.8',
        'dnbias 1',
        'nap 1',
        'dneb 3.1 3.1 3.1 3.1 3.1 3.1',
        'dgeb 3.1 3.1 3.1 3.1 3.1 3.1',
        'pecut 3.1',
        'hlcut 3.1',
        'sample correlate',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'dnbias 11',
        'hello',
    ]
