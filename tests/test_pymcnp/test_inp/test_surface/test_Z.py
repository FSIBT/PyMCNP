import pymcnp
from .... import consts
from .... import classes


class Test_Z:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Z
        EXAMPLES_VALID = [
            {
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {'z1': 3.1, 'r1': 3.1, 'z2': 3.1, 'r2': 3.1, 'z3': 3.1, 'r3': 3.1},
            {'z1': consts.ast.types.REAL, 'r1': consts.ast.types.REAL, 'z2': consts.ast.types.REAL, 'r2': consts.ast.types.REAL, 'z3': consts.ast.types.REAL, 'r3': consts.ast.types.REAL},
            {'z1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'z2': None, 'r2': consts.string.types.REAL, 'z3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'z1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'z2': consts.string.types.REAL, 'r2': None, 'z3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'z1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'z2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'z3': None, 'r3': consts.string.types.REAL},
            {'z1': consts.string.types.REAL, 'r1': consts.string.types.REAL, 'z2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'z3': consts.string.types.REAL, 'r3': None},
        ]
        EXAMPLES_INVALID = [
            {'z1': None, 'r1': consts.string.types.REAL, 'z2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'z3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
            {'z1': consts.string.types.REAL, 'r1': None, 'z2': consts.string.types.REAL, 'r2': consts.string.types.REAL, 'z3': consts.string.types.REAL, 'r3': consts.string.types.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Z
        EXAMPLES_VALID = [consts.string.inp.surface.Z]
        EXAMPLES_INVALID = ['hello']
