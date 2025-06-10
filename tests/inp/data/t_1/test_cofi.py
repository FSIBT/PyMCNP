import pymcnp
from .... import _utils


class Test_Cofi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cofi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.CofiBuilder
        EXAMPLES_VALID = [{'time': _utils.string.type.REAL}, {'time': 3.1}, {'time': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'time': None}]
