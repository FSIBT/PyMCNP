import pymcnp
from .... import consts
from .... import classes


class Test_Y:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Y
        EXAMPLES_VALID = [
            {
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {'y1': 3.1, 'r1': 3.1, 'y2': 3.1, 'r2': 3.1, 'y3': 3.1, 'r3': 3.1},
            {'y1': consts.ast.types.REAL, 'r1': consts.ast.types.REAL, 'y2': consts.ast.types.REAL, 'r2': consts.ast.types.REAL, 'y3': consts.ast.types.REAL, 'r3': consts.ast.types.REAL},
            {'y1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'y2': None, 'r2': consts.string.types.REAL, 'y3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'y1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'y2': consts.string.types.REAL, 'r2': None, 'y3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'y1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'y2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'y3': None, 'r3': consts.string.types.REAL},
            {'y1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'y2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'y3': consts.string.types.REAL, 'r3': None},
        ]
        EXAMPLES_INVALID = [
            {'y1': None, 'r1': consts.string.types.REAL, 'y2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'y3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'y1': consts.string.types.REAL, 'r1': None, 'y2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'y3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Y
        EXAMPLES_VALID = [consts.string.inp.surface.Y]
        EXAMPLES_INVALID = ['hello']
