import pymcnp
from .... import _utils


class Test_Ext:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.ExtBuilder
        EXAMPLES_VALID = [{'distance_cosine': _utils.string.type.REAL}, {'distance_cosine': 3.1}, {'distance_cosine': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'distance_cosine': None}]
