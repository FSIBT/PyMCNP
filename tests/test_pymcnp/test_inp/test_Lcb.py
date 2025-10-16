import pymcnp
from ... import consts
from ... import classes


class Test_Lcb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Lcb
        EXAMPLES_VALID = [
            {
                'flenb1': consts.string.types.REAL,
                'flenb2': consts.string.types.REAL,
                'flenb3': consts.string.types.REAL,
                'flenb4': consts.string.types.REAL,
                'flenb5': consts.string.types.REAL,
                'flenb6': consts.string.types.REAL,
                'cotfe': consts.string.types.REAL,
                'film0': consts.string.types.REAL,
            },
            {'flenb1': 3.1, 'flenb2': 3.1, 'flenb3': 3.1, 'flenb4': 3.1, 'flenb5': 3.1, 'flenb6': 3.1, 'cotfe': 3.1, 'film0': 3.1},
            {
                'flenb1': consts.ast.types.REAL,
                'flenb2': consts.ast.types.REAL,
                'flenb3': consts.ast.types.REAL,
                'flenb4': consts.ast.types.REAL,
                'flenb5': consts.ast.types.REAL,
                'flenb6': consts.ast.types.REAL,
                'cotfe': consts.ast.types.REAL,
                'film0': consts.ast.types.REAL,
            },
            {
                'flenb1': None,
                'flenb2': consts.string.types.REAL,
                'flenb3': consts.string.types.REAL,
                'flenb4': consts.string.types.REAL,
                'flenb5': consts.string.types.REAL,
                'flenb6': consts.string.types.REAL,
                'cotfe': consts.string.types.REAL,
                'film0': consts.string.types.REAL,
            },
            {
                'flenb1': consts.string.types.REAL,
                'flenb2': None,
                'flenb3': consts.string.types.REAL,
                'flenb4': consts.string.types.REAL,
                'flenb5': consts.string.types.REAL,
                'flenb6': consts.string.types.REAL,
                'cotfe': consts.string.types.REAL,
                'film0': consts.string.types.REAL,
            },
            {
                'flenb1': consts.string.types.REAL,
                'flenb2': consts.string.types.REAL,
                'flenb3': None,
                'flenb4': consts.string.types.REAL,
                'flenb5': consts.string.types.REAL,
                'flenb6': consts.string.types.REAL,
                'cotfe': consts.string.types.REAL,
                'film0': consts.string.types.REAL,
            },
            {
                'flenb1': consts.string.types.REAL,
                'flenb2': consts.string.types.REAL,
                'flenb3': consts.string.types.REAL,
                'flenb4': None,
                'flenb5': consts.string.types.REAL,
                'flenb6': consts.string.types.REAL,
                'cotfe': consts.string.types.REAL,
                'film0': consts.string.types.REAL,
            },
            {
                'flenb1': consts.string.types.REAL,
                'flenb2': consts.string.types.REAL,
                'flenb3': consts.string.types.REAL,
                'flenb4': consts.string.types.REAL,
                'flenb5': None,
                'flenb6': consts.string.types.REAL,
                'cotfe': consts.string.types.REAL,
                'film0': consts.string.types.REAL,
            },
            {
                'flenb1': consts.string.types.REAL,
                'flenb2': consts.string.types.REAL,
                'flenb3': consts.string.types.REAL,
                'flenb4': consts.string.types.REAL,
                'flenb5': consts.string.types.REAL,
                'flenb6': None,
                'cotfe': consts.string.types.REAL,
                'film0': consts.string.types.REAL,
            },
            {
                'flenb1': consts.string.types.REAL,
                'flenb2': consts.string.types.REAL,
                'flenb3': consts.string.types.REAL,
                'flenb4': consts.string.types.REAL,
                'flenb5': consts.string.types.REAL,
                'flenb6': consts.string.types.REAL,
                'cotfe': None,
                'film0': consts.string.types.REAL,
            },
            {
                'flenb1': consts.string.types.REAL,
                'flenb2': consts.string.types.REAL,
                'flenb3': consts.string.types.REAL,
                'flenb4': consts.string.types.REAL,
                'flenb5': consts.string.types.REAL,
                'flenb6': consts.string.types.REAL,
                'cotfe': consts.string.types.REAL,
                'film0': None,
            },
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Lcb
        EXAMPLES_VALID = [consts.string.inp.LCB]
        EXAMPLES_INVALID = ['hello']
