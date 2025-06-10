import pymcnp
from .... import _utils


class Test_Y:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.YBuilder
        EXAMPLES_VALID = [{'y_coordinate': _utils.string.type.REAL}, {'y_coordinate': 3.1}, {'y_coordinate': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'y_coordinate': None}]
