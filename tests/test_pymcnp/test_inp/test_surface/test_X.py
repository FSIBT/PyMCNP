import pymcnp
from .... import consts
from .... import classes


class Test_X:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.X
        EXAMPLES_VALID = [
            {
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {'x1': 3.1, 'r1': 3.1, 'x2': 3.1, 'r2': 3.1, 'x3': 3.1, 'r3': 3.1},
            {'x1': consts.ast.types.REAL, 'r1': consts.ast.types.REAL, 'x2': consts.ast.types.REAL, 'r2': consts.ast.types.REAL, 'x3': consts.ast.types.REAL, 'r3': consts.ast.types.REAL},
            {'x1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'x2': None, 'r2': consts.string.types.REAL, 'x3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'x1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'x2': consts.string.types.REAL, 'r2': None, 'x3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'x1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'x2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'x3': None, 'r3': consts.string.types.REAL},
            {'x1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'x2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'x3': consts.string.types.REAL, 'r3': None},
        ]
        EXAMPLES_INVALID = [
            {'x1': None, 'r1': consts.string.types.REAL, 'x2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'x3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'x1': consts.string.types.REAL, 'r1': None, 'x2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'x3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.X
        EXAMPLES_VALID = [consts.string.inp.surface.X]
        EXAMPLES_INVALID = ['hello']
