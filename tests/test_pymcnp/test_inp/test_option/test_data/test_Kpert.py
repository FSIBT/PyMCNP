import pymcnp
from ..... import classes


class Test_Kpert(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Kpert
    EXAMPLES_VALID = [
        'cell 1 1 1',
        'mat 1 1 1',
        'rho 3.1 3.1 3.1',
        'iso 001001 001001 001001',
        'rxn 1 1 1',
        'erg 3.1 3.1 3.1',
        'linear yes',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
