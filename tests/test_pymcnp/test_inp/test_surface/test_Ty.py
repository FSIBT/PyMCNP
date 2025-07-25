import pymcnp
from .... import consts
from .... import classes


class Test_Ty:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Ty
        EXAMPLES_VALID = [
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'a': consts.string.types.REAL, 'b': consts.string.types.REAL, 'c': consts.string.types.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1, 'a': 3.1, 'b': 3.1, 'c': 3.1},
            {'x': consts.ast.types.REAL, 'y': consts.ast.types.REAL, 'z': consts.ast.types.REAL, 'a': consts.ast.types.REAL, 'b': consts.ast.types.REAL, 'c': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'a': consts.string.types.REAL, 'b': consts.string.types.REAL, 'c': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': None, 'z': consts.string.types.REAL, 'a': consts.string.types.REAL, 'b': consts.string.types.REAL, 'c': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': None, 'a': consts.string.types.REAL, 'b': consts.string.types.REAL, 'c': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'a': None, 'b': consts.string.types.REAL, 'c': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'a': consts.string.types.REAL, 'b': None, 'c': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'a': consts.string.types.REAL, 'b': consts.string.types.REAL, 'c': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Ty
        EXAMPLES_VALID = [consts.string.inp.surface.TY]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Ty
        EXAMPLES = [consts.string.inp.surface.TY]
