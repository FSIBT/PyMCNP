import pymcnp
from .... import _utils


class Test_Width:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Width
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.WidthBuilder
        EXAMPLES_VALID = [{'width': _utils.string.type.REAL}, {'width': 3.1}, {'width': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'width': None}]
