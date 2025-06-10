import pymcnp
from ... import _utils


class Test_K_y:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.K_y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.K_yBuilder
        EXAMPLES_VALID = [
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 't_squared': _utils.string.type.REAL, 'plusminus_1': _utils.string.type.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {'x': _utils.ast.type.REAL, 'y': _utils.ast.type.REAL, 'z': _utils.ast.type.REAL, 't_squared': _utils.ast.type.REAL, 'plusminus_1': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 't_squared': _utils.string.type.REAL, 'plusminus_1': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': None, 'z': _utils.string.type.REAL, 't_squared': _utils.string.type.REAL, 'plusminus_1': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': None, 't_squared': _utils.string.type.REAL, 'plusminus_1': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 't_squared': None, 'plusminus_1': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 't_squared': _utils.string.type.REAL, 'plusminus_1': None},
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.K_y
        EXAMPLES = ['k/y 1 2 3 4 5']
