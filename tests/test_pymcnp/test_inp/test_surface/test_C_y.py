import pymcnp
from .... import consts
from .... import classes


class Test_C_y:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.C_y
        EXAMPLES_VALID = [
            {'x': consts.string.types.REAL, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'x': 3.1, 'z': 3.1, 'r': 3.1},
            {'x': consts.ast.types.REAL, 'z': consts.ast.types.REAL, 'r': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'z': None, 'r': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'z': consts.string.types.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.C_y
        EXAMPLES_VALID = [consts.string.inp.surface.C_Y]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.C_y
        EXAMPLES = [consts.string.inp.surface.C_Y]
