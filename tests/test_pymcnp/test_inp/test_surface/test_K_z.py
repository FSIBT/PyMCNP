import pymcnp
from .... import consts
from .... import classes


class Test_K_z:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.K_z
        EXAMPLES_VALID = [
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {'x': consts.ast.types.REAL, 'y': consts.ast.types.REAL, 'z': consts.ast.types.REAL, 't_squared': consts.ast.types.REAL, 'plusminus_1': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': None, 'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': None, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 't_squared': None, 'plusminus_1': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.K_z
        EXAMPLES_VALID = [consts.string.inp.surface.K_Z]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.K_z
        EXAMPLES = [consts.string.inp.surface.K_Z]
