import pymcnp
from .... import consts
from .... import classes


class Test_P_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.P_1
        EXAMPLES_VALID = [
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {'x1': 3.1, 'y1': 3.1, 'z1': 3.1, 'x2': 3.1, 'y2': 3.1, 'z2': 3.1, 'x3': 3.1, 'y3': 3.1, 'z3': 3.1},
            {
                'x1': consts.ast.types.REAL,
                'y1': consts.ast.types.REAL,
                'z1': consts.ast.types.REAL,
                'x2': consts.ast.types.REAL,
                'y2': consts.ast.types.REAL,
                'z2': consts.ast.types.REAL,
                'x3': consts.ast.types.REAL,
                'y3': consts.ast.types.REAL,
                'z3': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x1': None,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': None,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': None,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': None,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': None,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': None,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': None,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': None,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.P_1
        EXAMPLES_VALID = [consts.string.inp.surface.P_1]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.P_1
        EXAMPLES = [consts.string.inp.surface.P_1]
