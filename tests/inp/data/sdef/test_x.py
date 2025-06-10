import pymcnp
from .... import _utils


class Test_X:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.X
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.XBuilder
        EXAMPLES_VALID = [{'x_coordinate': _utils.string.type.REAL}, {'x_coordinate': 3.1}, {'x_coordinate': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'x_coordinate': None}]
