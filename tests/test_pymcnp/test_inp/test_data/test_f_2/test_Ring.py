import pymcnp
from ..... import consts
from ..... import classes


class Test_Ring:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.f_2.Ring
        EXAMPLES_VALID = [
            {
                'distance': consts.string.type.REAL,
                'radius': consts.string.type.REAL,
                'ro': consts.string.type.INTEGER,
            },
            {
                'distance': 0.5,
                'radius': 0.5,
                'ro': 1,
            },
            {
                'distance': consts.ast.type.REAL,
                'radius': consts.ast.type.REAL,
                'ro': consts.ast.type.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'distance': None,
                'radius': consts.string.type.REAL,
                'ro': consts.string.type.INTEGER,
            },
            {
                'distance': consts.string.type.REAL,
                'radius': None,
                'ro': consts.string.type.INTEGER,
            },
            {
                'distance': consts.string.type.REAL,
                'radius': consts.string.type.REAL,
                'ro': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.f_2.Ring
        EXAMPLES_VALID = [consts.string.inp.data.f_2.RING]
        EXAMPLES_INVALID = ['hello']
