import pymcnp
from .... import _utils


class Test_Cfrq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cfrq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.CfrqBuilder
        EXAMPLES_VALID = [{'frequency': _utils.string.type.REAL}, {'frequency': 3.1}, {'frequency': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'frequency': None}]
