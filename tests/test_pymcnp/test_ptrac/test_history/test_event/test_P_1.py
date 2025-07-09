import pymcnp
from ..... import consts
from ..... import classes


class Test_P_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.event.P_1
        EXAMPLES_VALID = [
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'u': consts.ast.type.REAL,
                'v': consts.ast.type.REAL,
                'w': consts.ast.type.REAL,
                'erg': consts.ast.type.REAL,
                'wgt': consts.ast.type.REAL,
                'tme': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'u': consts.ast.type.REAL,
                'v': consts.ast.type.REAL,
                'w': consts.ast.type.REAL,
                'erg': consts.ast.type.REAL,
                'wgt': consts.ast.type.REAL,
                'tme': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': None,
                'z': consts.ast.type.REAL,
                'u': consts.ast.type.REAL,
                'v': consts.ast.type.REAL,
                'w': consts.ast.type.REAL,
                'erg': consts.ast.type.REAL,
                'wgt': consts.ast.type.REAL,
                'tme': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': None,
                'u': consts.ast.type.REAL,
                'v': consts.ast.type.REAL,
                'w': consts.ast.type.REAL,
                'erg': consts.ast.type.REAL,
                'wgt': consts.ast.type.REAL,
                'tme': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'u': None,
                'v': consts.ast.type.REAL,
                'w': consts.ast.type.REAL,
                'erg': consts.ast.type.REAL,
                'wgt': consts.ast.type.REAL,
                'tme': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'u': consts.ast.type.REAL,
                'v': None,
                'w': consts.ast.type.REAL,
                'erg': consts.ast.type.REAL,
                'wgt': consts.ast.type.REAL,
                'tme': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'u': consts.ast.type.REAL,
                'v': consts.ast.type.REAL,
                'w': None,
                'erg': consts.ast.type.REAL,
                'wgt': consts.ast.type.REAL,
                'tme': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'u': consts.ast.type.REAL,
                'v': consts.ast.type.REAL,
                'w': consts.ast.type.REAL,
                'erg': None,
                'wgt': consts.ast.type.REAL,
                'tme': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'u': consts.ast.type.REAL,
                'v': consts.ast.type.REAL,
                'w': consts.ast.type.REAL,
                'erg': consts.ast.type.REAL,
                'wgt': None,
                'tme': consts.ast.type.REAL,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'u': consts.ast.type.REAL,
                'v': consts.ast.type.REAL,
                'w': consts.ast.type.REAL,
                'erg': consts.ast.type.REAL,
                'wgt': consts.ast.type.REAL,
                'tme': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.event.P_1
        EXAMPLES_VALID = [consts.string.ptrac.history.event.P_1]
        EXAMPLES_INVALID = ['hello']
