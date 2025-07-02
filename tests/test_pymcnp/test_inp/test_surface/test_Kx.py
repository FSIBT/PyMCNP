import pymcnp
from .... import consts
from .... import classes


class Test_Kx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Kx
        EXAMPLES_VALID = [{'x': consts.ast.type.REAL, 't_squared': consts.ast.type.REAL, 'plusminus_1': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [
            {'x': None, 't_squared': consts.ast.type.REAL, 'plusminus_1': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 't_squared': None, 'plusminus_1': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 't_squared': consts.ast.type.REAL, 'plusminus_1': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Kx
        EXAMPLES_VALID = [consts.string.inp.surface.KX]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Kx
        EXAMPLES = [consts.string.inp.surface.KX]


class Test_KxBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.KxBuilder
        EXAMPLES_VALID = [
            {'x': consts.string.type.REAL, 't_squared': consts.string.type.REAL, 'plusminus_1': consts.string.type.REAL},
            {'x': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {'x': consts.ast.type.REAL, 't_squared': consts.ast.type.REAL, 'plusminus_1': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 't_squared': consts.string.type.REAL, 'plusminus_1': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 't_squared': None, 'plusminus_1': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 't_squared': consts.string.type.REAL, 'plusminus_1': None},
        ]
