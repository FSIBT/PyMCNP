import pymcnp
from ..... import consts
from ..... import classes


class Test_P_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.event.P_1
        EXAMPLES_VALID = [
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'u': consts.ast.types.REAL,
                'v': consts.ast.types.REAL,
                'w': consts.ast.types.REAL,
                'erg': consts.ast.types.REAL,
                'wgt': consts.ast.types.REAL,
                'tme': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'u': consts.ast.types.REAL,
                'v': consts.ast.types.REAL,
                'w': consts.ast.types.REAL,
                'erg': consts.ast.types.REAL,
                'wgt': consts.ast.types.REAL,
                'tme': consts.ast.types.REAL,
            },
            {
                'x': consts.ast.types.REAL,
                'y': None,
                'z': consts.ast.types.REAL,
                'u': consts.ast.types.REAL,
                'v': consts.ast.types.REAL,
                'w': consts.ast.types.REAL,
                'erg': consts.ast.types.REAL,
                'wgt': consts.ast.types.REAL,
                'tme': consts.ast.types.REAL,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': None,
                'u': consts.ast.types.REAL,
                'v': consts.ast.types.REAL,
                'w': consts.ast.types.REAL,
                'erg': consts.ast.types.REAL,
                'wgt': consts.ast.types.REAL,
                'tme': consts.ast.types.REAL,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'u': None,
                'v': consts.ast.types.REAL,
                'w': consts.ast.types.REAL,
                'erg': consts.ast.types.REAL,
                'wgt': consts.ast.types.REAL,
                'tme': consts.ast.types.REAL,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'u': consts.ast.types.REAL,
                'v': None,
                'w': consts.ast.types.REAL,
                'erg': consts.ast.types.REAL,
                'wgt': consts.ast.types.REAL,
                'tme': consts.ast.types.REAL,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'u': consts.ast.types.REAL,
                'v': consts.ast.types.REAL,
                'w': None,
                'erg': consts.ast.types.REAL,
                'wgt': consts.ast.types.REAL,
                'tme': consts.ast.types.REAL,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'u': consts.ast.types.REAL,
                'v': consts.ast.types.REAL,
                'w': consts.ast.types.REAL,
                'erg': None,
                'wgt': consts.ast.types.REAL,
                'tme': consts.ast.types.REAL,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'u': consts.ast.types.REAL,
                'v': consts.ast.types.REAL,
                'w': consts.ast.types.REAL,
                'erg': consts.ast.types.REAL,
                'wgt': None,
                'tme': consts.ast.types.REAL,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'u': consts.ast.types.REAL,
                'v': consts.ast.types.REAL,
                'w': consts.ast.types.REAL,
                'erg': consts.ast.types.REAL,
                'wgt': consts.ast.types.REAL,
                'tme': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.event.P_1
        EXAMPLES_VALID = [consts.string.ptrac.history.event.P_1]
        EXAMPLES_INVALID = ['hello']
