import pymcnp
from .... import _utils


class Test_Set:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Set
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.SetBuilder
        EXAMPLES_VALID = [
            {
                'f': _utils.string.type.INTEGER,
                'd': _utils.string.type.INTEGER,
                'u': _utils.string.type.INTEGER,
                's': _utils.string.type.INTEGER,
                'm': _utils.string.type.INTEGER,
                'c': _utils.string.type.INTEGER,
                'e': _utils.string.type.INTEGER,
                't': _utils.string.type.INTEGER,
            },
            {'f': 1, 'd': 1, 'u': 1, 's': 1, 'm': 1, 'c': 1, 'e': 1, 't': 1},
            {
                'f': _utils.ast.type.INTEGER,
                'd': _utils.ast.type.INTEGER,
                'u': _utils.ast.type.INTEGER,
                's': _utils.ast.type.INTEGER,
                'm': _utils.ast.type.INTEGER,
                'c': _utils.ast.type.INTEGER,
                'e': _utils.ast.type.INTEGER,
                't': _utils.ast.type.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'f': None,
                'd': _utils.string.type.INTEGER,
                'u': _utils.string.type.INTEGER,
                's': _utils.string.type.INTEGER,
                'm': _utils.string.type.INTEGER,
                'c': _utils.string.type.INTEGER,
                'e': _utils.string.type.INTEGER,
                't': _utils.string.type.INTEGER,
            },
            {
                'f': _utils.string.type.INTEGER,
                'd': None,
                'u': _utils.string.type.INTEGER,
                's': _utils.string.type.INTEGER,
                'm': _utils.string.type.INTEGER,
                'c': _utils.string.type.INTEGER,
                'e': _utils.string.type.INTEGER,
                't': _utils.string.type.INTEGER,
            },
            {
                'f': _utils.string.type.INTEGER,
                'd': _utils.string.type.INTEGER,
                'u': None,
                's': _utils.string.type.INTEGER,
                'm': _utils.string.type.INTEGER,
                'c': _utils.string.type.INTEGER,
                'e': _utils.string.type.INTEGER,
                't': _utils.string.type.INTEGER,
            },
            {
                'f': _utils.string.type.INTEGER,
                'd': _utils.string.type.INTEGER,
                'u': _utils.string.type.INTEGER,
                's': None,
                'm': _utils.string.type.INTEGER,
                'c': _utils.string.type.INTEGER,
                'e': _utils.string.type.INTEGER,
                't': _utils.string.type.INTEGER,
            },
            {
                'f': _utils.string.type.INTEGER,
                'd': _utils.string.type.INTEGER,
                'u': _utils.string.type.INTEGER,
                's': _utils.string.type.INTEGER,
                'm': None,
                'c': _utils.string.type.INTEGER,
                'e': _utils.string.type.INTEGER,
                't': _utils.string.type.INTEGER,
            },
            {
                'f': _utils.string.type.INTEGER,
                'd': _utils.string.type.INTEGER,
                'u': _utils.string.type.INTEGER,
                's': _utils.string.type.INTEGER,
                'm': _utils.string.type.INTEGER,
                'c': None,
                'e': _utils.string.type.INTEGER,
                't': _utils.string.type.INTEGER,
            },
            {
                'f': _utils.string.type.INTEGER,
                'd': _utils.string.type.INTEGER,
                'u': _utils.string.type.INTEGER,
                's': _utils.string.type.INTEGER,
                'm': _utils.string.type.INTEGER,
                'c': _utils.string.type.INTEGER,
                'e': None,
                't': _utils.string.type.INTEGER,
            },
            {
                'f': _utils.string.type.INTEGER,
                'd': _utils.string.type.INTEGER,
                'u': _utils.string.type.INTEGER,
                's': _utils.string.type.INTEGER,
                'm': _utils.string.type.INTEGER,
                'c': _utils.string.type.INTEGER,
                'e': _utils.string.type.INTEGER,
                't': None,
            },
        ]
