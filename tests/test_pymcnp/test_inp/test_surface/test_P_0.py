import pymcnp
from .... import consts
from .... import classes


class Test_P_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.P_0
        EXAMPLES_VALID = [
            {'a': consts.string.type.REAL, 'b': consts.string.type.REAL, 'c': consts.string.type.REAL, 'd': consts.string.type.REAL},
            {'a': 3.1, 'b': 3.1, 'c': 3.1, 'd': 3.1},
            {'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL, 'c': consts.ast.type.REAL, 'd': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'b': consts.string.type.REAL, 'c': consts.string.type.REAL, 'd': consts.string.type.REAL},
            {'a': consts.string.type.REAL, 'b': None, 'c': consts.string.type.REAL, 'd': consts.string.type.REAL},
            {'a': consts.string.type.REAL, 'b': consts.string.type.REAL, 'c': None, 'd': consts.string.type.REAL},
            {'a': consts.string.type.REAL, 'b': consts.string.type.REAL, 'c': consts.string.type.REAL, 'd': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.P_0
        EXAMPLES_VALID = [consts.string.inp.surface.P_0]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.P_0
        EXAMPLES = [consts.string.inp.surface.P_0]
