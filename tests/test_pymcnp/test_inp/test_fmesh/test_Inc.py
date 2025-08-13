import pymcnp
from .... import consts
from .... import classes


class Test_Inc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmesh.Inc
        EXAMPLES_VALID = [
            {'lower': consts.string.types.REAL, 'upper': consts.string.types.REAL},
            {'lower': 3.1, 'upper': 3.1},
            {'lower': consts.ast.types.REAL, 'upper': consts.ast.types.REAL},
            {'lower': consts.string.types.REAL, 'upper': None},
        ]
        EXAMPLES_INVALID = [{'lower': None, 'upper': consts.string.types.REAL}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmesh.Inc
        EXAMPLES_VALID = [consts.string.inp.fmesh.INC]
        EXAMPLES_INVALID = ['hello']
