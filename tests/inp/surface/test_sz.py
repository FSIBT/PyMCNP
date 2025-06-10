import pymcnp
from ... import _utils


class Test_Sz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SzBuilder
        EXAMPLES_VALID = [{'z': _utils.string.type.REAL, 'r': _utils.string.type.REAL}, {'z': 3.1, 'r': 3.1}, {'z': _utils.ast.type.REAL, 'r': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'z': None, 'r': _utils.string.type.REAL}, {'z': _utils.string.type.REAL, 'r': None}]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Sz
        EXAMPLES = [
            'sz 3 1',
        ]
