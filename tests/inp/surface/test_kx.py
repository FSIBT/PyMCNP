import pymcnp
from ... import _utils


class Test_Kx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Kx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.KxBuilder
        EXAMPLES_VALID = [
            {'x': _utils.string.type.REAL, 't_squared': _utils.string.type.REAL, 'plusminus_1': _utils.string.type.REAL},
            {'x': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {'x': _utils.ast.type.REAL, 't_squared': _utils.ast.type.REAL, 'plusminus_1': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 't_squared': _utils.string.type.REAL, 'plusminus_1': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 't_squared': None, 'plusminus_1': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 't_squared': _utils.string.type.REAL, 'plusminus_1': None},
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Kx
        EXAMPLES = ['kx 1 2 3']
