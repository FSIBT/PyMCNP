import pymcnp
from .... import consts
from .... import classes


class Test_C_y:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.C_y
        EXAMPLES_VALID = [{'x': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [
            {'x': None, 'z': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'z': None, 'r': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.C_y
        EXAMPLES_VALID = [consts.string.inp.surface.C_Y]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.C_y
        EXAMPLES = [consts.string.inp.surface.C_Y]


class Test_C_yBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.C_yBuilder
        EXAMPLES_VALID = [
            {'x': consts.string.type.REAL, 'z': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'x': 3.1, 'z': 3.1, 'r': 3.1},
            {'x': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'z': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'z': None, 'r': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'z': consts.string.type.REAL, 'r': None},
        ]
