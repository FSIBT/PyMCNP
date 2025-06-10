import pymcnp
from ... import _utils


class Test_Sx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SxBuilder
        EXAMPLES_VALID = [{'x': _utils.string.type.REAL, 'r': _utils.string.type.REAL}, {'x': 3.1, 'r': 3.1}, {'x': _utils.ast.type.REAL, 'r': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'x': None, 'r': _utils.string.type.REAL}, {'x': _utils.string.type.REAL, 'r': None}]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Sx
        EXAMPLES = [
            'sx 3 1',
        ]
