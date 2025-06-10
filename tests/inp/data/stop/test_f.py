import pymcnp
from .... import _utils


class Test_F:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.stop.F
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.stop.FBuilder
        EXAMPLES_VALID = [{'suffix': _utils.string.type.INTEGER, 'e': _utils.string.type.INTEGER}, {'suffix': 1, 'e': 1}, {'suffix': _utils.ast.type.INTEGER, 'e': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'suffix': None, 'e': _utils.string.type.INTEGER}, {'suffix': _utils.string.type.INTEGER, 'e': None}]
