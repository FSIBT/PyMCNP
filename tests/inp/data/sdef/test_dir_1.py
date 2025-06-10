import pymcnp
from .... import _utils


class Test_Dir_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dir_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.DirBuilder_1
        EXAMPLES_VALID = [{'cosine': _utils.string.type.DISTRIBUTIONNUMBER}, {'cosine': _utils.ast.type.DISTRIBUTIONNUMBER}, {'cosine': None}]
        EXAMPLES_INVALID = []
