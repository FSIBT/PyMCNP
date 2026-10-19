import pymcnp
from ..... import classes


class Test_Pert(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Pert
    EXAMPLES_VALID = [
        'cell 1 1 1',
        'mat 1',
        'rho 3.1',
        'method 1',
        'erg 3.1 3.1',
        'rxn 1 1 1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
