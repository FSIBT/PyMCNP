import pymcnp
from .... import consts
from .... import classes


class Test_P_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.P_0
        EXAMPLES_VALID = [
            {'a': consts.string.types.REAL, 'b': consts.string.types.REAL, 'c': consts.string.types.REAL, 'd': consts.string.types.REAL},
            {'a': 3.1, 'b': 3.1, 'c': 3.1, 'd': 3.1},
            {'a': consts.ast.types.REAL, 'b': consts.ast.types.REAL, 'c': consts.ast.types.REAL, 'd': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'b': consts.string.types.REAL, 'c': consts.string.types.REAL, 'd': consts.string.types.REAL},
            {'a': consts.string.types.REAL, 'b': None, 'c': consts.string.types.REAL, 'd': consts.string.types.REAL},
            {'a': consts.string.types.REAL, 'b': consts.string.types.REAL, 'c': None, 'd': consts.string.types.REAL},
            {'a': consts.string.types.REAL, 'b': consts.string.types.REAL, 'c': consts.string.types.REAL, 'd': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.P_0
        EXAMPLES_VALID = [consts.string.inp.surface.P_0]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.P_0
        EXAMPLES = [consts.string.inp.surface.P_0]
