import pymcnp
from ... import _utils


class Test_X:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.X
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.XBuilder
        EXAMPLES_VALID = [
            {'x1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'x2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'x3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'x1': 3.1, 'r1': 3.1, 'x2': 3.1, 'r2': 3.1, 'x3': 3.1, 'r3': 3.1},
            {'x1': _utils.ast.type.REAL, 'r1': _utils.ast.type.REAL, 'x2': _utils.ast.type.REAL, 'r2': _utils.ast.type.REAL, 'x3': _utils.ast.type.REAL, 'r3': _utils.ast.type.REAL},
            {'x1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'x2': None, 'r2': _utils.string.type.REAL, 'x3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'x1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'x2': _utils.string.type.REAL, 'r2': None, 'x3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'x1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'x2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'x3': None, 'r3': _utils.string.type.REAL},
            {'x1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'x2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'x3': _utils.string.type.REAL, 'r3': None},
        ]
        EXAMPLES_INVALID = [
            {'x1': None, 'r1': _utils.string.type.REAL, 'x2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'x3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'x1': _utils.string.type.REAL, 'r1': None, 'x2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'x3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
        ]
