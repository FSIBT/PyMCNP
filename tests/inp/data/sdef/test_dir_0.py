import pymcnp
from .... import _utils


class Test_Dir_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dir_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.DirBuilder_0
        EXAMPLES_VALID = [{'cosine': _utils.string.type.REAL}, {'cosine': 3.1}, {'cosine': _utils.ast.type.REAL}, {'cosine': None}]
        EXAMPLES_INVALID = []
