import pymcnp
from ..... import classes


class Test_Mesh(classes.Test_FromMcnp):
    element = pymcnp.inp.option.data.Mesh
    EXAMPLES_FROM_MCNP_VALID = [
        'geom xyz',
        'ref 3.1 3.1 3.1',
        'origin 3.1 3.1 3.1',
        'axs 3.1 3.1 3.1',
        'vec 3.1 3.1 3.1',
        'imesh 3.1 3.1 3.1',
        'iints 1 1 1',
        'jmesh 3.1 3.1 3.1',
        'jints 1 1 1',
        'kmesh 3.1 3.1 3.1',
        'kints 1 1 1',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]
