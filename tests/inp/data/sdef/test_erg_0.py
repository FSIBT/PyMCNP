import pymcnp
from .... import _utils


class Test_Erg_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Erg_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.ErgBuilder_0
        EXAMPLES_VALID = [{'energy': _utils.string.type.REAL}, {'energy': 3.1}, {'energy': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]
