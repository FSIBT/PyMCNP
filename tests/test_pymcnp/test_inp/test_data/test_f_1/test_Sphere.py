import pymcnp
from ..... import consts
from ..... import classes


class Test_Sphere:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.f_1.Sphere
        EXAMPLES_VALID = [
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': consts.string.type.INTEGER,
                'ro': consts.string.type.INTEGER,
            },
            {
                'x': 0.5,
                'y': 0.5,
                'z': 1,
                'ro': 1,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.INTEGER,
                'ro': consts.ast.type.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.string.type.REAL,
                'z': consts.string.type.INTEGER,
                'ro': consts.string.type.INTEGER,
            },
            {
                'x': consts.string.type.REAL,
                'y': None,
                'z': consts.string.type.INTEGER,
                'ro': consts.string.type.INTEGER,
            },
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': None,
                'ro': consts.string.type.INTEGER,
            },
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': consts.string.type.INTEGER,
                'ro': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.f_1.Sphere
        EXAMPLES_VALID = [consts.string.inp.data.f_1.SPHERE]
        EXAMPLES_INVALID = ['hello']
