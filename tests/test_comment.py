import pymcnp
import _utils


class Test_Comment:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Comment
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []
