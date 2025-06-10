import pymcnp
from ... import _utils


class Test_Y:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.YBuilder
        EXAMPLES_VALID = [
            {'y1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'y2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'y3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'y1': 3.1, 'r1': 3.1, 'y2': 3.1, 'r2': 3.1, 'y3': 3.1, 'r3': 3.1},
            {'y1': _utils.ast.type.REAL, 'r1': _utils.ast.type.REAL, 'y2': _utils.ast.type.REAL, 'r2': _utils.ast.type.REAL, 'y3': _utils.ast.type.REAL, 'r3': _utils.ast.type.REAL},
            {'y1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'y2': None, 'r2': _utils.string.type.REAL, 'y3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'y1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'y2': _utils.string.type.REAL, 'r2': None, 'y3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'y1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'y2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'y3': None, 'r3': _utils.string.type.REAL},
            {'y1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'y2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'y3': _utils.string.type.REAL, 'r3': None},
        ]
        EXAMPLES_INVALID = [
            {'y1': None, 'r1': _utils.string.type.REAL, 'y2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'y3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'y1': _utils.string.type.REAL, 'r1': None, 'y2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'y3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
        ]
