import pymcnp
from ... import _utils


class Test_P_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.P_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.PBuilder_1
        EXAMPLES_VALID = [
            {
                'x1': _utils.string.type.REAL,
                'y1': _utils.string.type.REAL,
                'z1': _utils.string.type.REAL,
                'x2': _utils.string.type.REAL,
                'y2': _utils.string.type.REAL,
                'z2': _utils.string.type.REAL,
                'x3': _utils.string.type.REAL,
                'y3': _utils.string.type.REAL,
                'z3': _utils.string.type.REAL,
            },
            {'x1': 3.1, 'y1': 3.1, 'z1': 3.1, 'x2': 3.1, 'y2': 3.1, 'z2': 3.1, 'x3': 3.1, 'y3': 3.1, 'z3': 3.1},
            {
                'x1': _utils.ast.type.REAL,
                'y1': _utils.ast.type.REAL,
                'z1': _utils.ast.type.REAL,
                'x2': _utils.ast.type.REAL,
                'y2': _utils.ast.type.REAL,
                'z2': _utils.ast.type.REAL,
                'x3': _utils.ast.type.REAL,
                'y3': _utils.ast.type.REAL,
                'z3': _utils.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x1': None,
                'y1': _utils.string.type.REAL,
                'z1': _utils.string.type.REAL,
                'x2': _utils.string.type.REAL,
                'y2': _utils.string.type.REAL,
                'z2': _utils.string.type.REAL,
                'x3': _utils.string.type.REAL,
                'y3': _utils.string.type.REAL,
                'z3': _utils.string.type.REAL,
            },
            {
                'x1': _utils.string.type.REAL,
                'y1': None,
                'z1': _utils.string.type.REAL,
                'x2': _utils.string.type.REAL,
                'y2': _utils.string.type.REAL,
                'z2': _utils.string.type.REAL,
                'x3': _utils.string.type.REAL,
                'y3': _utils.string.type.REAL,
                'z3': _utils.string.type.REAL,
            },
            {
                'x1': _utils.string.type.REAL,
                'y1': _utils.string.type.REAL,
                'z1': None,
                'x2': _utils.string.type.REAL,
                'y2': _utils.string.type.REAL,
                'z2': _utils.string.type.REAL,
                'x3': _utils.string.type.REAL,
                'y3': _utils.string.type.REAL,
                'z3': _utils.string.type.REAL,
            },
            {
                'x1': _utils.string.type.REAL,
                'y1': _utils.string.type.REAL,
                'z1': _utils.string.type.REAL,
                'x2': None,
                'y2': _utils.string.type.REAL,
                'z2': _utils.string.type.REAL,
                'x3': _utils.string.type.REAL,
                'y3': _utils.string.type.REAL,
                'z3': _utils.string.type.REAL,
            },
            {
                'x1': _utils.string.type.REAL,
                'y1': _utils.string.type.REAL,
                'z1': _utils.string.type.REAL,
                'x2': _utils.string.type.REAL,
                'y2': None,
                'z2': _utils.string.type.REAL,
                'x3': _utils.string.type.REAL,
                'y3': _utils.string.type.REAL,
                'z3': _utils.string.type.REAL,
            },
            {
                'x1': _utils.string.type.REAL,
                'y1': _utils.string.type.REAL,
                'z1': _utils.string.type.REAL,
                'x2': _utils.string.type.REAL,
                'y2': _utils.string.type.REAL,
                'z2': None,
                'x3': _utils.string.type.REAL,
                'y3': _utils.string.type.REAL,
                'z3': _utils.string.type.REAL,
            },
            {
                'x1': _utils.string.type.REAL,
                'y1': _utils.string.type.REAL,
                'z1': _utils.string.type.REAL,
                'x2': _utils.string.type.REAL,
                'y2': _utils.string.type.REAL,
                'z2': _utils.string.type.REAL,
                'x3': None,
                'y3': _utils.string.type.REAL,
                'z3': _utils.string.type.REAL,
            },
            {
                'x1': _utils.string.type.REAL,
                'y1': _utils.string.type.REAL,
                'z1': _utils.string.type.REAL,
                'x2': _utils.string.type.REAL,
                'y2': _utils.string.type.REAL,
                'z2': _utils.string.type.REAL,
                'x3': _utils.string.type.REAL,
                'y3': None,
                'z3': _utils.string.type.REAL,
            },
            {
                'x1': _utils.string.type.REAL,
                'y1': _utils.string.type.REAL,
                'z1': _utils.string.type.REAL,
                'x2': _utils.string.type.REAL,
                'y2': _utils.string.type.REAL,
                'z2': _utils.string.type.REAL,
                'x3': _utils.string.type.REAL,
                'y3': _utils.string.type.REAL,
                'z3': None,
            },
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.P_1
        EXAMPLES = [
            'p 1 0 0 2 0 0 3 0 0',
        ]
