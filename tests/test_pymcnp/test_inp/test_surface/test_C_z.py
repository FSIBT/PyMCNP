import pymcnp
from .... import consts
from .... import classes


class Test_C_z:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.C_z
        EXAMPLES_VALID = [{'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': None, 'r': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.C_z
        EXAMPLES_VALID = [consts.string.inp.surface.C_Z]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.C_z
        EXAMPLES = [consts.string.inp.surface.C_Z]


class Test_C_zBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.C_zBuilder
        EXAMPLES_VALID = [
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'x': 3.1, 'y': 3.1, 'r': 3.1},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': None, 'r': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'r': None},
        ]
