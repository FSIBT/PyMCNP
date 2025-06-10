import pymcnp
from .... import _utils


class Test_Length:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Length
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.LengthBuilder
        EXAMPLES_VALID = [{'factor': _utils.string.type.REAL}, {'factor': 3.1}, {'factor': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]
