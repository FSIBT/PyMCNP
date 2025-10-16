import pymcnp
from .... import consts
from .... import classes


class Test_Ring:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.f_2.Ring
        EXAMPLES_VALID = [
            {
                'distance': consts.string.types.REAL,
                'radius': consts.string.types.REAL,
                'ro': consts.string.types.INTEGER,
            },
            {
                'distance': 0.5,
                'radius': 0.5,
                'ro': 1,
            },
            {
                'distance': consts.ast.types.REAL,
                'radius': consts.ast.types.REAL,
                'ro': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'distance': None,
                'radius': consts.string.types.REAL,
                'ro': consts.string.types.INTEGER,
            },
            {
                'distance': consts.string.types.REAL,
                'radius': None,
                'ro': consts.string.types.INTEGER,
            },
            {
                'distance': consts.string.types.REAL,
                'radius': consts.string.types.REAL,
                'ro': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.f_2.Ring
        EXAMPLES_VALID = [consts.string.inp.f_2.RING]
        EXAMPLES_INVALID = ['hello']
