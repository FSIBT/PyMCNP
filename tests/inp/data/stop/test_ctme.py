import pymcnp
from .... import _utils


class Test_Ctme:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.stop.Ctme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.stop.CtmeBuilder
        EXAMPLES_VALID = [{'tme': _utils.string.type.REAL}, {'tme': 3.1}, {'tme': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'tme': None}]
