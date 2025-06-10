import pymcnp
from .... import _utils


class Test_Maxstep:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Maxstep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.MaxstepBuilder
        EXAMPLES_VALID = [{'size': _utils.string.type.REAL}, {'size': 3.1}, {'size': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'size': None}]
