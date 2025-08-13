import pymcnp
from .... import consts
from .... import classes


class Test_Origin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmesh.Origin
        EXAMPLES_VALID = [
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1},
            {'x': consts.ast.types.REAL, 'y': consts.ast.types.REAL, 'z': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': None, 'z': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmesh.Origin
        EXAMPLES_VALID = [consts.string.inp.fmesh.ORIGIN]
        EXAMPLES_INVALID = ['hello']
