import pymcnp
from .... import _utils


class Test_Psc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Psc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.PscBuilder
        EXAMPLES_VALID = [{'constant': _utils.string.type.REAL}, {'constant': 3.1}, {'constant': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'constant': None}]
