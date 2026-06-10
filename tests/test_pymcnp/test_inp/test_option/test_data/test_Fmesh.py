import pymcnp
from ..... import classes


class Test_Fmesh(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Fmesh
    EXAMPLES_VALID = [
        'geom xyz',
        'origin 3.1 3.1 3.1',
        'axs 3.1 3.1 3.1',
        'vec 3.1 3.1 3.1',
        'imesh 3.1 3.1 3.1',
        'iints 1 1 1',
        'jmesh 3.1 3.1 3.1',
        'jints 1 1 1',
        'kmesh 3.1 3.1 3.1',
        'kints 1 1 1',
        'emesh 3.1',
        'eints 1',
        'enorm yes',
        'tmesh 3.1',
        'tints 1',
        'tnorm yes',
        'factor 3.1',
        'out col',
        'tr 1',
        'inc',
        'inc 1',
        'inc 1 1',
        'inc 1 infinite',
        'type flux',
        'kclear 1',
        'tally hist',
        'tally batch',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
