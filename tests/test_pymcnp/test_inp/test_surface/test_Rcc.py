import pymcnp
from .... import consts
from .... import classes


class Test_Rcc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES_VALID = [
            {
                'vx': consts.ast.type.REAL,
                'vy': consts.ast.type.REAL,
                'vz': consts.ast.type.REAL,
                'hx': consts.ast.type.REAL,
                'hy': consts.ast.type.REAL,
                'hz': consts.ast.type.REAL,
                'r': consts.ast.type.REAL,
            }
        ]
        EXAMPLES_INVALID = [
            {'vx': None, 'vy': consts.ast.type.REAL, 'vz': consts.ast.type.REAL, 'hx': consts.ast.type.REAL, 'hy': consts.ast.type.REAL, 'hz': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
            {'vx': consts.ast.type.REAL, 'vy': None, 'vz': consts.ast.type.REAL, 'hx': consts.ast.type.REAL, 'hy': consts.ast.type.REAL, 'hz': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
            {'vx': consts.ast.type.REAL, 'vy': consts.ast.type.REAL, 'vz': None, 'hx': consts.ast.type.REAL, 'hy': consts.ast.type.REAL, 'hz': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
            {'vx': consts.ast.type.REAL, 'vy': consts.ast.type.REAL, 'vz': consts.ast.type.REAL, 'hx': None, 'hy': consts.ast.type.REAL, 'hz': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
            {'vx': consts.ast.type.REAL, 'vy': consts.ast.type.REAL, 'vz': consts.ast.type.REAL, 'hx': consts.ast.type.REAL, 'hy': None, 'hz': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
            {'vx': consts.ast.type.REAL, 'vy': consts.ast.type.REAL, 'vz': consts.ast.type.REAL, 'hx': consts.ast.type.REAL, 'hy': consts.ast.type.REAL, 'hz': None, 'r': consts.ast.type.REAL},
            {'vx': consts.ast.type.REAL, 'vy': consts.ast.type.REAL, 'vz': consts.ast.type.REAL, 'hx': consts.ast.type.REAL, 'hy': consts.ast.type.REAL, 'hz': consts.ast.type.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES_VALID = [consts.string.inp.surface.RCC]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES = [consts.string.inp.surface.RCC]


class Test_RccBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.RccBuilder
        EXAMPLES_VALID = [
            {
                'vx': consts.string.type.REAL,
                'vy': consts.string.type.REAL,
                'vz': consts.string.type.REAL,
                'hx': consts.string.type.REAL,
                'hy': consts.string.type.REAL,
                'hz': consts.string.type.REAL,
                'r': consts.string.type.REAL,
            },
            {'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'hx': 3.1, 'hy': 3.1, 'hz': 3.1, 'r': 3.1},
            {
                'vx': consts.ast.type.REAL,
                'vy': consts.ast.type.REAL,
                'vz': consts.ast.type.REAL,
                'hx': consts.ast.type.REAL,
                'hy': consts.ast.type.REAL,
                'hz': consts.ast.type.REAL,
                'r': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': None,
                'vy': consts.string.type.REAL,
                'vz': consts.string.type.REAL,
                'hx': consts.string.type.REAL,
                'hy': consts.string.type.REAL,
                'hz': consts.string.type.REAL,
                'r': consts.string.type.REAL,
            },
            {
                'vx': consts.string.type.REAL,
                'vy': None,
                'vz': consts.string.type.REAL,
                'hx': consts.string.type.REAL,
                'hy': consts.string.type.REAL,
                'hz': consts.string.type.REAL,
                'r': consts.string.type.REAL,
            },
            {
                'vx': consts.string.type.REAL,
                'vy': consts.string.type.REAL,
                'vz': None,
                'hx': consts.string.type.REAL,
                'hy': consts.string.type.REAL,
                'hz': consts.string.type.REAL,
                'r': consts.string.type.REAL,
            },
            {
                'vx': consts.string.type.REAL,
                'vy': consts.string.type.REAL,
                'vz': consts.string.type.REAL,
                'hx': None,
                'hy': consts.string.type.REAL,
                'hz': consts.string.type.REAL,
                'r': consts.string.type.REAL,
            },
            {
                'vx': consts.string.type.REAL,
                'vy': consts.string.type.REAL,
                'vz': consts.string.type.REAL,
                'hx': consts.string.type.REAL,
                'hy': None,
                'hz': consts.string.type.REAL,
                'r': consts.string.type.REAL,
            },
            {
                'vx': consts.string.type.REAL,
                'vy': consts.string.type.REAL,
                'vz': consts.string.type.REAL,
                'hx': consts.string.type.REAL,
                'hy': consts.string.type.REAL,
                'hz': None,
                'r': consts.string.type.REAL,
            },
            {
                'vx': consts.string.type.REAL,
                'vy': consts.string.type.REAL,
                'vz': consts.string.type.REAL,
                'hx': consts.string.type.REAL,
                'hy': consts.string.type.REAL,
                'hz': consts.string.type.REAL,
                'r': None,
            },
        ]
