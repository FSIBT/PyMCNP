import pymcnp
from .... import consts
from .... import classes


class Test_K_x:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.K_x
        EXAMPLES_VALID = [{'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 't_squared': consts.ast.type.REAL, 'plusminus_1': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 't_squared': consts.ast.type.REAL, 'plusminus_1': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': None, 'z': consts.ast.type.REAL, 't_squared': consts.ast.type.REAL, 'plusminus_1': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': None, 't_squared': consts.ast.type.REAL, 'plusminus_1': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 't_squared': None, 'plusminus_1': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 't_squared': consts.ast.type.REAL, 'plusminus_1': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.K_x
        EXAMPLES_VALID = [consts.string.inp.surface.K_X]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.K_x
        EXAMPLES = [consts.string.inp.surface.K_X]


class Test_K_xBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.K_xBuilder
        EXAMPLES_VALID = [
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 't_squared': consts.string.type.REAL, 'plusminus_1': consts.string.type.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 't_squared': consts.ast.type.REAL, 'plusminus_1': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 't_squared': consts.string.type.REAL, 'plusminus_1': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': None, 'z': consts.string.type.REAL, 't_squared': consts.string.type.REAL, 'plusminus_1': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': None, 't_squared': consts.string.type.REAL, 'plusminus_1': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 't_squared': None, 'plusminus_1': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 't_squared': consts.string.type.REAL, 'plusminus_1': None},
        ]
