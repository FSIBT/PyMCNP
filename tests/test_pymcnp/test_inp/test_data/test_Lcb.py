import pymcnp
from .... import consts
from .... import classes


class Test_Lcb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Lcb
        EXAMPLES_VALID = [
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': consts.ast.type.REAL,
                'flenb3': consts.ast.type.REAL,
                'flenb4': consts.ast.type.REAL,
                'flenb5': consts.ast.type.REAL,
                'flenb6': consts.ast.type.REAL,
                'cotfe': consts.ast.type.REAL,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': None,
                'flenb2': consts.ast.type.REAL,
                'flenb3': consts.ast.type.REAL,
                'flenb4': consts.ast.type.REAL,
                'flenb5': consts.ast.type.REAL,
                'flenb6': consts.ast.type.REAL,
                'cotfe': consts.ast.type.REAL,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': None,
                'flenb3': consts.ast.type.REAL,
                'flenb4': consts.ast.type.REAL,
                'flenb5': consts.ast.type.REAL,
                'flenb6': consts.ast.type.REAL,
                'cotfe': consts.ast.type.REAL,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': consts.ast.type.REAL,
                'flenb3': None,
                'flenb4': consts.ast.type.REAL,
                'flenb5': consts.ast.type.REAL,
                'flenb6': consts.ast.type.REAL,
                'cotfe': consts.ast.type.REAL,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': consts.ast.type.REAL,
                'flenb3': consts.ast.type.REAL,
                'flenb4': None,
                'flenb5': consts.ast.type.REAL,
                'flenb6': consts.ast.type.REAL,
                'cotfe': consts.ast.type.REAL,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': consts.ast.type.REAL,
                'flenb3': consts.ast.type.REAL,
                'flenb4': consts.ast.type.REAL,
                'flenb5': None,
                'flenb6': consts.ast.type.REAL,
                'cotfe': consts.ast.type.REAL,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': consts.ast.type.REAL,
                'flenb3': consts.ast.type.REAL,
                'flenb4': consts.ast.type.REAL,
                'flenb5': consts.ast.type.REAL,
                'flenb6': None,
                'cotfe': consts.ast.type.REAL,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': consts.ast.type.REAL,
                'flenb3': consts.ast.type.REAL,
                'flenb4': consts.ast.type.REAL,
                'flenb5': consts.ast.type.REAL,
                'flenb6': consts.ast.type.REAL,
                'cotfe': None,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': consts.ast.type.REAL,
                'flenb3': consts.ast.type.REAL,
                'flenb4': consts.ast.type.REAL,
                'flenb5': consts.ast.type.REAL,
                'flenb6': consts.ast.type.REAL,
                'cotfe': consts.ast.type.REAL,
                'film0': None,
            },
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Lcb
        EXAMPLES_VALID = [consts.string.inp.data.LCB]
        EXAMPLES_INVALID = ['hello']


class Test_LcbBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.LcbBuilder
        EXAMPLES_VALID = [
            {
                'flenb1': consts.string.type.REAL,
                'flenb2': consts.string.type.REAL,
                'flenb3': consts.string.type.REAL,
                'flenb4': consts.string.type.REAL,
                'flenb5': consts.string.type.REAL,
                'flenb6': consts.string.type.REAL,
                'cotfe': consts.string.type.REAL,
                'film0': consts.string.type.REAL,
            },
            {'flenb1': 3.1, 'flenb2': 3.1, 'flenb3': 3.1, 'flenb4': 3.1, 'flenb5': 3.1, 'flenb6': 3.1, 'cotfe': 3.1, 'film0': 3.1},
            {
                'flenb1': consts.ast.type.REAL,
                'flenb2': consts.ast.type.REAL,
                'flenb3': consts.ast.type.REAL,
                'flenb4': consts.ast.type.REAL,
                'flenb5': consts.ast.type.REAL,
                'flenb6': consts.ast.type.REAL,
                'cotfe': consts.ast.type.REAL,
                'film0': consts.ast.type.REAL,
            },
            {
                'flenb1': None,
                'flenb2': consts.string.type.REAL,
                'flenb3': consts.string.type.REAL,
                'flenb4': consts.string.type.REAL,
                'flenb5': consts.string.type.REAL,
                'flenb6': consts.string.type.REAL,
                'cotfe': consts.string.type.REAL,
                'film0': consts.string.type.REAL,
            },
            {
                'flenb1': consts.string.type.REAL,
                'flenb2': None,
                'flenb3': consts.string.type.REAL,
                'flenb4': consts.string.type.REAL,
                'flenb5': consts.string.type.REAL,
                'flenb6': consts.string.type.REAL,
                'cotfe': consts.string.type.REAL,
                'film0': consts.string.type.REAL,
            },
            {
                'flenb1': consts.string.type.REAL,
                'flenb2': consts.string.type.REAL,
                'flenb3': None,
                'flenb4': consts.string.type.REAL,
                'flenb5': consts.string.type.REAL,
                'flenb6': consts.string.type.REAL,
                'cotfe': consts.string.type.REAL,
                'film0': consts.string.type.REAL,
            },
            {
                'flenb1': consts.string.type.REAL,
                'flenb2': consts.string.type.REAL,
                'flenb3': consts.string.type.REAL,
                'flenb4': None,
                'flenb5': consts.string.type.REAL,
                'flenb6': consts.string.type.REAL,
                'cotfe': consts.string.type.REAL,
                'film0': consts.string.type.REAL,
            },
            {
                'flenb1': consts.string.type.REAL,
                'flenb2': consts.string.type.REAL,
                'flenb3': consts.string.type.REAL,
                'flenb4': consts.string.type.REAL,
                'flenb5': None,
                'flenb6': consts.string.type.REAL,
                'cotfe': consts.string.type.REAL,
                'film0': consts.string.type.REAL,
            },
            {
                'flenb1': consts.string.type.REAL,
                'flenb2': consts.string.type.REAL,
                'flenb3': consts.string.type.REAL,
                'flenb4': consts.string.type.REAL,
                'flenb5': consts.string.type.REAL,
                'flenb6': None,
                'cotfe': consts.string.type.REAL,
                'film0': consts.string.type.REAL,
            },
            {
                'flenb1': consts.string.type.REAL,
                'flenb2': consts.string.type.REAL,
                'flenb3': consts.string.type.REAL,
                'flenb4': consts.string.type.REAL,
                'flenb5': consts.string.type.REAL,
                'flenb6': consts.string.type.REAL,
                'cotfe': None,
                'film0': consts.string.type.REAL,
            },
            {
                'flenb1': consts.string.type.REAL,
                'flenb2': consts.string.type.REAL,
                'flenb3': consts.string.type.REAL,
                'flenb4': consts.string.type.REAL,
                'flenb5': consts.string.type.REAL,
                'flenb6': consts.string.type.REAL,
                'cotfe': consts.string.type.REAL,
                'film0': None,
            },
        ]
        EXAMPLES_INVALID = []
