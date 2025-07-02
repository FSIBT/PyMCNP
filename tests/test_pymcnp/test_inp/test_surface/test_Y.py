import pymcnp
from .... import consts
from .... import classes


class Test_Y:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Y
        EXAMPLES_VALID = [
            {'y1': consts.ast.type.REAL, 'r1': consts.ast.type.REAL, 'y2': consts.ast.type.REAL, 'r2': consts.ast.type.REAL, 'y3': consts.ast.type.REAL, 'r3': consts.ast.type.REAL},
            {'y1': consts.ast.type.REAL, 'r1': consts.ast.type.REAL, 'y2': None, 'r2': consts.ast.type.REAL, 'y3': consts.ast.type.REAL, 'r3': consts.ast.type.REAL},
            {'y1': consts.ast.type.REAL, 'r1': consts.ast.type.REAL, 'y2': consts.ast.type.REAL, 'r2': None, 'y3': consts.ast.type.REAL, 'r3': consts.ast.type.REAL},
            {'y1': consts.ast.type.REAL, 'r1': consts.ast.type.REAL, 'y2': consts.ast.type.REAL, 'r2': consts.ast.type.REAL, 'y3': None, 'r3': consts.ast.type.REAL},
            {'y1': consts.ast.type.REAL, 'r1': consts.ast.type.REAL, 'y2': consts.ast.type.REAL, 'r2': consts.ast.type.REAL, 'y3': consts.ast.type.REAL, 'r3': None},
        ]
        EXAMPLES_INVALID = [
            {'y1': None, 'r1': consts.ast.type.REAL, 'y2': consts.ast.type.REAL, 'r2': consts.ast.type.REAL, 'y3': consts.ast.type.REAL, 'r3': consts.ast.type.REAL},
            {'y1': consts.ast.type.REAL, 'r1': None, 'y2': consts.ast.type.REAL, 'r2': consts.ast.type.REAL, 'y3': consts.ast.type.REAL, 'r3': consts.ast.type.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Y
        EXAMPLES_VALID = [consts.string.inp.surface.Y]
        EXAMPLES_INVALID = ['hello']


class Test_YBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.YBuilder
        EXAMPLES_VALID = [
            {'y1': consts.string.type.REAL, 'r1': consts.string.type.REAL, 'y2': consts.string.type.REAL, 'r2': consts.string.type.REAL, 'y3': consts.string.type.REAL, 'r3': consts.string.type.REAL},
            {'y1': 3.1, 'r1': 3.1, 'y2': 3.1, 'r2': 3.1, 'y3': 3.1, 'r3': 3.1},
            {'y1': consts.ast.type.REAL, 'r1': consts.ast.type.REAL, 'y2': consts.ast.type.REAL, 'r2': consts.ast.type.REAL, 'y3': consts.ast.type.REAL, 'r3': consts.ast.type.REAL},
            {'y1': consts.string.type.REAL, 'r1': consts.string.type.REAL, 'y2': None, 'r2': consts.string.type.REAL, 'y3': consts.string.type.REAL, 'r3': consts.string.type.REAL},
            {'y1': consts.string.type.REAL, 'r1': consts.string.type.REAL, 'y2': consts.string.type.REAL, 'r2': None, 'y3': consts.string.type.REAL, 'r3': consts.string.type.REAL},
            {'y1': consts.string.type.REAL, 'r1': consts.string.type.REAL, 'y2': consts.string.type.REAL, 'r2': consts.string.type.REAL, 'y3': None, 'r3': consts.string.type.REAL},
            {'y1': consts.string.type.REAL, 'r1': consts.string.type.REAL, 'y2': consts.string.type.REAL, 'r2': consts.string.type.REAL, 'y3': consts.string.type.REAL, 'r3': None},
        ]
        EXAMPLES_INVALID = [
            {'y1': None, 'r1': consts.string.type.REAL, 'y2': consts.string.type.REAL, 'r2': consts.string.type.REAL, 'y3': consts.string.type.REAL, 'r3': consts.string.type.REAL},
            {'y1': consts.string.type.REAL, 'r1': None, 'y2': consts.string.type.REAL, 'r2': consts.string.type.REAL, 'y3': consts.string.type.REAL, 'r3': consts.string.type.REAL},
        ]
