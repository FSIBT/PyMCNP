import pymcnp
from .... import consts
from .... import classes


class Test_Rcc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES_VALID = [
            {
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'hx': consts.string.types.REAL,
                'hy': consts.string.types.REAL,
                'hz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'hx': 3.1, 'hy': 3.1, 'hz': 3.1, 'r': 3.1},
            {
                'vx': consts.ast.types.REAL,
                'vy': consts.ast.types.REAL,
                'vz': consts.ast.types.REAL,
                'hx': consts.ast.types.REAL,
                'hy': consts.ast.types.REAL,
                'hz': consts.ast.types.REAL,
                'r': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': None,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'hx': consts.string.types.REAL,
                'hy': consts.string.types.REAL,
                'hz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'vx': consts.string.types.REAL,
                'vy': None,
                'vz': consts.string.types.REAL,
                'hx': consts.string.types.REAL,
                'hy': consts.string.types.REAL,
                'hz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': None,
                'hx': consts.string.types.REAL,
                'hy': consts.string.types.REAL,
                'hz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'hx': None,
                'hy': consts.string.types.REAL,
                'hz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'hx': consts.string.types.REAL,
                'hy': None,
                'hz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'hx': consts.string.types.REAL,
                'hy': consts.string.types.REAL,
                'hz': None,
                'r': consts.string.types.REAL,
            },
            {
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'hx': consts.string.types.REAL,
                'hy': consts.string.types.REAL,
                'hz': consts.string.types.REAL,
                'r': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES_VALID = [consts.string.inp.surface.RCC]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES = [consts.string.inp.surface.RCC]
