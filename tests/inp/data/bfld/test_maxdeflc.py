import pymcnp
from .... import _utils


class Test_Maxdeflc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Maxdeflc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.MaxdeflcBuilder
        EXAMPLES_VALID = [{'angle': _utils.string.type.REAL}, {'angle': 3.1}, {'angle': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'angle': None}]
