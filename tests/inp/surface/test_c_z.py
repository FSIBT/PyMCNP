import pymcnp
from ... import _utils


class Test_C_z:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.C_z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.C_zBuilder
        EXAMPLES_VALID = [
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'r': _utils.string.type.REAL},
            {'x': 3.1, 'y': 3.1, 'r': 3.1},
            {'x': _utils.ast.type.REAL, 'y': _utils.ast.type.REAL, 'r': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': _utils.string.type.REAL, 'r': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': None, 'r': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'r': None},
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.C_z
        EXAMPLES = [
            'c/z 1 4 3',
        ]
