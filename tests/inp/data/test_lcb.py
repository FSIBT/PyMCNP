import pymcnp
from ... import _utils


class Test_Lcb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lcb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.LcbBuilder
        EXAMPLES_VALID = [
            {
                'flenb1': _utils.string.type.REAL,
                'flenb2': _utils.string.type.REAL,
                'flenb3': _utils.string.type.REAL,
                'flenb4': _utils.string.type.REAL,
                'flenb5': _utils.string.type.REAL,
                'flenb6': _utils.string.type.REAL,
                'cotfe': _utils.string.type.REAL,
                'film0': _utils.string.type.REAL,
            },
            {'flenb1': 3.1, 'flenb2': 3.1, 'flenb3': 3.1, 'flenb4': 3.1, 'flenb5': 3.1, 'flenb6': 3.1, 'cotfe': 3.1, 'film0': 3.1},
            {
                'flenb1': _utils.ast.type.REAL,
                'flenb2': _utils.ast.type.REAL,
                'flenb3': _utils.ast.type.REAL,
                'flenb4': _utils.ast.type.REAL,
                'flenb5': _utils.ast.type.REAL,
                'flenb6': _utils.ast.type.REAL,
                'cotfe': _utils.ast.type.REAL,
                'film0': _utils.ast.type.REAL,
            },
            {
                'flenb1': None,
                'flenb2': _utils.string.type.REAL,
                'flenb3': _utils.string.type.REAL,
                'flenb4': _utils.string.type.REAL,
                'flenb5': _utils.string.type.REAL,
                'flenb6': _utils.string.type.REAL,
                'cotfe': _utils.string.type.REAL,
                'film0': _utils.string.type.REAL,
            },
            {
                'flenb1': _utils.string.type.REAL,
                'flenb2': None,
                'flenb3': _utils.string.type.REAL,
                'flenb4': _utils.string.type.REAL,
                'flenb5': _utils.string.type.REAL,
                'flenb6': _utils.string.type.REAL,
                'cotfe': _utils.string.type.REAL,
                'film0': _utils.string.type.REAL,
            },
            {
                'flenb1': _utils.string.type.REAL,
                'flenb2': _utils.string.type.REAL,
                'flenb3': None,
                'flenb4': _utils.string.type.REAL,
                'flenb5': _utils.string.type.REAL,
                'flenb6': _utils.string.type.REAL,
                'cotfe': _utils.string.type.REAL,
                'film0': _utils.string.type.REAL,
            },
            {
                'flenb1': _utils.string.type.REAL,
                'flenb2': _utils.string.type.REAL,
                'flenb3': _utils.string.type.REAL,
                'flenb4': None,
                'flenb5': _utils.string.type.REAL,
                'flenb6': _utils.string.type.REAL,
                'cotfe': _utils.string.type.REAL,
                'film0': _utils.string.type.REAL,
            },
            {
                'flenb1': _utils.string.type.REAL,
                'flenb2': _utils.string.type.REAL,
                'flenb3': _utils.string.type.REAL,
                'flenb4': _utils.string.type.REAL,
                'flenb5': None,
                'flenb6': _utils.string.type.REAL,
                'cotfe': _utils.string.type.REAL,
                'film0': _utils.string.type.REAL,
            },
            {
                'flenb1': _utils.string.type.REAL,
                'flenb2': _utils.string.type.REAL,
                'flenb3': _utils.string.type.REAL,
                'flenb4': _utils.string.type.REAL,
                'flenb5': _utils.string.type.REAL,
                'flenb6': None,
                'cotfe': _utils.string.type.REAL,
                'film0': _utils.string.type.REAL,
            },
            {
                'flenb1': _utils.string.type.REAL,
                'flenb2': _utils.string.type.REAL,
                'flenb3': _utils.string.type.REAL,
                'flenb4': _utils.string.type.REAL,
                'flenb5': _utils.string.type.REAL,
                'flenb6': _utils.string.type.REAL,
                'cotfe': None,
                'film0': _utils.string.type.REAL,
            },
            {
                'flenb1': _utils.string.type.REAL,
                'flenb2': _utils.string.type.REAL,
                'flenb3': _utils.string.type.REAL,
                'flenb4': _utils.string.type.REAL,
                'flenb5': _utils.string.type.REAL,
                'flenb6': _utils.string.type.REAL,
                'cotfe': _utils.string.type.REAL,
                'film0': None,
            },
        ]
        EXAMPLES_INVALID = []
