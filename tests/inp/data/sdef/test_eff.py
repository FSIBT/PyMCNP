import pymcnp
from .... import _utils


class Test_Eff:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Eff
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.EffBuilder
        EXAMPLES_VALID = [{'criterion': _utils.string.type.REAL}, {'criterion': 3.1}, {'criterion': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'criterion': None}]
