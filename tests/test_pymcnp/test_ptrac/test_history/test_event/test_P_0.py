import pymcnp
from ..... import consts
from ..... import classes


class Test_P_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.event.P_0
        EXAMPLES_VALID = [
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': None,
                'z': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.event.P_0
        EXAMPLES_VALID = [consts.string.ptrac.history.event.P_0]
        EXAMPLES_INVALID = ['hello']
