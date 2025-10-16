import pymcnp
from .... import consts
from .... import classes


class Test_Location:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ksrc.Location
        EXAMPLES_VALID = [
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
            },
            {
                'x': 0.5,
                'y': 0.5,
                'z': 0.5,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
            },
            {
                'x': consts.string.types.REAL,
                'y': None,
                'z': consts.string.types.REAL,
            },
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ksrc.Location
        EXAMPLES_VALID = [consts.string.inp.ksrc.LOCATION]
        EXAMPLES_INVALID = ['hello']
