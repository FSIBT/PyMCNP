import pymcnp
from ... import _utils


class Test_Pz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Pz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.PzBuilder
        EXAMPLES_VALID = [{'d': _utils.string.type.REAL}, {'d': 3.1}, {'d': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'d': None}]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Pz
        EXAMPLES = [
            'pz 1',
        ]
