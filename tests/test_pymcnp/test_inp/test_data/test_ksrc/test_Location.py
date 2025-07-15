import pymcnp
from ..... import consts
from ..... import classes


class Test_Location:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ksrc.Location
        EXAMPLES_VALID = [
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': consts.string.type.REAL,
            },
            {
                'x': 0.5,
                'y': 0.5,
                'z': 0.5,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.string.type.REAL,
                'z': consts.string.type.REAL,
            },
            {
                'x': consts.string.type.REAL,
                'y': None,
                'z': consts.string.type.REAL,
            },
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ksrc.Location
        EXAMPLES_VALID = [consts.string.inp.data.ksrc.LOCATION]
        EXAMPLES_INVALID = ['hello']
