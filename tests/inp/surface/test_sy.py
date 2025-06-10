import pymcnp
from ... import _utils


class Test_Sy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SyBuilder
        EXAMPLES_VALID = [{'y': _utils.string.type.REAL, 'r': _utils.string.type.REAL}, {'y': 3.1, 'r': 3.1}, {'y': _utils.ast.type.REAL, 'r': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'y': None, 'r': _utils.string.type.REAL}, {'y': _utils.string.type.REAL, 'r': None}]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Sy
        EXAMPLES = [
            'sy 3 1',
        ]
