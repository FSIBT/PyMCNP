import pymcnp
from .... import consts
from .... import classes


class Test_Sph:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Sph
        EXAMPLES_VALID = [
            {'vx': consts.string.type.REAL, 'vy': consts.string.type.REAL, 'vz': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'r': 3.1},
            {'vx': consts.ast.type.REAL, 'vy': consts.ast.type.REAL, 'vz': consts.ast.type.REAL, 'r': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'vx': None, 'vy': consts.string.type.REAL, 'vz': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'vx': consts.string.type.REAL, 'vy': None, 'vz': consts.string.type.REAL, 'r': consts.string.type.REAL},
            {'vx': consts.string.type.REAL, 'vy': consts.string.type.REAL, 'vz': None, 'r': consts.string.type.REAL},
            {'vx': consts.string.type.REAL, 'vy': consts.string.type.REAL, 'vz': consts.string.type.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Sph
        EXAMPLES_VALID = [consts.string.inp.surface.SPH]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Sph
        EXAMPLES = [consts.string.inp.surface.SPH]
