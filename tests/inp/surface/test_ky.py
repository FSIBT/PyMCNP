import pymcnp
from ... import _utils


class Test_Ky:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Ky
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.KyBuilder
        EXAMPLES_VALID = [
            {'y': _utils.string.type.REAL, 't_squared': _utils.string.type.REAL, 'plusminus_1': _utils.string.type.REAL},
            {'y': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {'y': _utils.ast.type.REAL, 't_squared': _utils.ast.type.REAL, 'plusminus_1': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'y': None, 't_squared': _utils.string.type.REAL, 'plusminus_1': _utils.string.type.REAL},
            {'y': _utils.string.type.REAL, 't_squared': None, 'plusminus_1': _utils.string.type.REAL},
            {'y': _utils.string.type.REAL, 't_squared': _utils.string.type.REAL, 'plusminus_1': None},
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Ky
        EXAMPLES = ['ky 1 2 3']
