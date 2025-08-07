import pymcnp
from .... import consts
from .... import classes


class Test_Sph:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Sph
        EXAMPLES_VALID = [
            {'vx': consts.string.types.REAL, 'vy': consts.string.types.REAL, 'vz': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'r': 3.1},
            {'vx': consts.ast.types.REAL, 'vy': consts.ast.types.REAL, 'vz': consts.ast.types.REAL, 'r': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'vx': None, 'vy': consts.string.types.REAL, 'vz': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'vx': consts.string.types.REAL, 'vy': None, 'vz': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'vx': consts.string.types.REAL, 'vy': consts.string.types.REAL, 'vz': None, 'r': consts.string.types.REAL},
            {'vx': consts.string.types.REAL, 'vy': consts.string.types.REAL, 'vz': consts.string.types.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Sph
        EXAMPLES_VALID = [consts.string.inp.surface.SPH]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Sph
        EXAMPLES = [consts.string.inp.surface.SPH]
