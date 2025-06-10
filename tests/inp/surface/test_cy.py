import pymcnp
from ... import _utils


class Test_Cy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Cy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.CyBuilder
        EXAMPLES_VALID = [{'r': _utils.string.type.REAL}, {'r': 3.1}, {'r': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'r': None}]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Cy
        EXAMPLES = [
            'cy 1',
        ]
