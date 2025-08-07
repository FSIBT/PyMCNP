import pymcnp
from .... import consts
from .... import classes


class Test_Kz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Kz
        EXAMPLES_VALID = [
            {'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'z': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {'z': consts.ast.types.REAL, 't_squared': consts.ast.types.REAL, 'plusminus_1': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'z': None, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'z': consts.string.types.REAL, 't_squared': None, 'plusminus_1': consts.string.types.REAL},
            {'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Kz
        EXAMPLES_VALID = [consts.string.inp.surface.KZ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Kz
        EXAMPLES = [consts.string.inp.surface.KZ]
