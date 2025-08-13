import pymcnp
from .... import consts
from .... import classes


class Test_Sphere:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.f_1.Sphere
        EXAMPLES_VALID = [
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.INTEGER,
                'ro': consts.string.types.INTEGER,
            },
            {
                'x': 0.5,
                'y': 0.5,
                'z': 1,
                'ro': 1,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.INTEGER,
                'ro': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.string.types.REAL,
                'z': consts.string.types.INTEGER,
                'ro': consts.string.types.INTEGER,
            },
            {
                'x': consts.string.types.REAL,
                'y': None,
                'z': consts.string.types.INTEGER,
                'ro': consts.string.types.INTEGER,
            },
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': None,
                'ro': consts.string.types.INTEGER,
            },
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.INTEGER,
                'ro': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.f_1.Sphere
        EXAMPLES_VALID = [consts.string.inp.f_1.SPHERE]
        EXAMPLES_INVALID = ['hello']
