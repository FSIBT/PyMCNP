import pymcnp
from .... import consts
from .... import classes


class Test_P_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.P_1
        EXAMPLES_VALID = [
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            }
        ]
        EXAMPLES_INVALID = [
            {
                'x1': None,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            },
            {
                'x1': consts.ast.type.REAL,
                'y1': None,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            },
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': None,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            },
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': None,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            },
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': None,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            },
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': None,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            },
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': None,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            },
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': None,
                'z3': consts.ast.type.REAL,
            },
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
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


class Test_PBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.PBuilder_1
        EXAMPLES_VALID = [
            {
                'x1': consts.string.type.REAL,
                'y1': consts.string.type.REAL,
                'z1': consts.string.type.REAL,
                'x2': consts.string.type.REAL,
                'y2': consts.string.type.REAL,
                'z2': consts.string.type.REAL,
                'x3': consts.string.type.REAL,
                'y3': consts.string.type.REAL,
                'z3': consts.string.type.REAL,
            },
            {'x1': 3.1, 'y1': 3.1, 'z1': 3.1, 'x2': 3.1, 'y2': 3.1, 'z2': 3.1, 'x3': 3.1, 'y3': 3.1, 'z3': 3.1},
            {
                'x1': consts.ast.type.REAL,
                'y1': consts.ast.type.REAL,
                'z1': consts.ast.type.REAL,
                'x2': consts.ast.type.REAL,
                'y2': consts.ast.type.REAL,
                'z2': consts.ast.type.REAL,
                'x3': consts.ast.type.REAL,
                'y3': consts.ast.type.REAL,
                'z3': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x1': None,
                'y1': consts.string.type.REAL,
                'z1': consts.string.type.REAL,
                'x2': consts.string.type.REAL,
                'y2': consts.string.type.REAL,
                'z2': consts.string.type.REAL,
                'x3': consts.string.type.REAL,
                'y3': consts.string.type.REAL,
                'z3': consts.string.type.REAL,
            },
            {
                'x1': consts.string.type.REAL,
                'y1': None,
                'z1': consts.string.type.REAL,
                'x2': consts.string.type.REAL,
                'y2': consts.string.type.REAL,
                'z2': consts.string.type.REAL,
                'x3': consts.string.type.REAL,
                'y3': consts.string.type.REAL,
                'z3': consts.string.type.REAL,
            },
            {
                'x1': consts.string.type.REAL,
                'y1': consts.string.type.REAL,
                'z1': None,
                'x2': consts.string.type.REAL,
                'y2': consts.string.type.REAL,
                'z2': consts.string.type.REAL,
                'x3': consts.string.type.REAL,
                'y3': consts.string.type.REAL,
                'z3': consts.string.type.REAL,
            },
            {
                'x1': consts.string.type.REAL,
                'y1': consts.string.type.REAL,
                'z1': consts.string.type.REAL,
                'x2': None,
                'y2': consts.string.type.REAL,
                'z2': consts.string.type.REAL,
                'x3': consts.string.type.REAL,
                'y3': consts.string.type.REAL,
                'z3': consts.string.type.REAL,
            },
            {
                'x1': consts.string.type.REAL,
                'y1': consts.string.type.REAL,
                'z1': consts.string.type.REAL,
                'x2': consts.string.type.REAL,
                'y2': None,
                'z2': consts.string.type.REAL,
                'x3': consts.string.type.REAL,
                'y3': consts.string.type.REAL,
                'z3': consts.string.type.REAL,
            },
            {
                'x1': consts.string.type.REAL,
                'y1': consts.string.type.REAL,
                'z1': consts.string.type.REAL,
                'x2': consts.string.type.REAL,
                'y2': consts.string.type.REAL,
                'z2': None,
                'x3': consts.string.type.REAL,
                'y3': consts.string.type.REAL,
                'z3': consts.string.type.REAL,
            },
            {
                'x1': consts.string.type.REAL,
                'y1': consts.string.type.REAL,
                'z1': consts.string.type.REAL,
                'x2': consts.string.type.REAL,
                'y2': consts.string.type.REAL,
                'z2': consts.string.type.REAL,
                'x3': None,
                'y3': consts.string.type.REAL,
                'z3': consts.string.type.REAL,
            },
            {
                'x1': consts.string.type.REAL,
                'y1': consts.string.type.REAL,
                'z1': consts.string.type.REAL,
                'x2': consts.string.type.REAL,
                'y2': consts.string.type.REAL,
                'z2': consts.string.type.REAL,
                'x3': consts.string.type.REAL,
                'y3': None,
                'z3': consts.string.type.REAL,
            },
            {
                'x1': consts.string.type.REAL,
                'y1': consts.string.type.REAL,
                'z1': consts.string.type.REAL,
                'x2': consts.string.type.REAL,
                'y2': consts.string.type.REAL,
                'z2': consts.string.type.REAL,
                'x3': consts.string.type.REAL,
                'y3': consts.string.type.REAL,
                'z3': None,
            },
        ]
