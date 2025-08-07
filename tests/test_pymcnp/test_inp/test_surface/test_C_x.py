import pymcnp
from .... import consts
from .... import classes


class Test_C_x:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.C_x
        EXAMPLES_VALID = [
            {'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'y': 3.1, 'z': 3.1, 'r': 3.1},
            {'y': consts.ast.types.REAL, 'z': consts.ast.types.REAL, 'r': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'y': None, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'y': consts.string.types.REAL, 'z': None, 'r': consts.string.types.REAL},
            {'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.C_x
        EXAMPLES_VALID = [consts.string.inp.surface.C_X]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.C_x
        EXAMPLES = [consts.string.inp.surface.C_X]
