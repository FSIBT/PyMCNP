import pymcnp
from .... import consts
from .... import classes


class Test_C_z:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.C_z
        EXAMPLES_VALID = [
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'x': 3.1, 'y': 3.1, 'r': 3.1},
            {'x': consts.ast.types.REAL, 'y': consts.ast.types.REAL, 'r': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': None, 'r': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.C_z
        EXAMPLES_VALID = [consts.string.inp.surface.C_Z]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.C_z
        EXAMPLES = [consts.string.inp.surface.C_Z]
