import pymcnp
from .... import consts
from .... import classes


class Test_Ky:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Ky
        EXAMPLES_VALID = [
            {'y': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'y': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {'y': consts.ast.types.REAL, 't_squared': consts.ast.types.REAL, 'plusminus_1': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'y': None, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'y': consts.string.types.REAL, 't_squared': None, 'plusminus_1': consts.string.types.REAL},
            {'y': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Ky
        EXAMPLES_VALID = [consts.string.inp.surface.KY]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Ky
        EXAMPLES = [consts.string.inp.surface.KY]
