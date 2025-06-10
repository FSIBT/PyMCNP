import pymcnp
from .... import _utils


class Test_Ara:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Ara
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.AraBuilder
        EXAMPLES_VALID = [{'area': _utils.string.type.REAL}, {'area': 3.1}, {'area': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'area': None}]
