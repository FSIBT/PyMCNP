import pymcnp
from .... import consts
from .... import classes


class Test_C_x:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.C_x
        EXAMPLES_VALID = [
            {'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'y': 3.1, 'z': 3.1, 'r': 3.1},
            {'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'y': None, 'z': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'y': consts.string.type.REAL, 'z': None, 'r': consts.string.type.REAL},
            {'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.C_x
        EXAMPLES_VALID = [consts.string.inp.surface.C_X]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.C_x
        EXAMPLES = [consts.string.inp.surface.C_X]
