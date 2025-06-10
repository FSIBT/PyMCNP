import pymcnp
from .... import _utils


class Test_Value:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Value
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.ValueBuilder
        EXAMPLES_VALID = [{'cutoff': _utils.string.type.REAL}, {'cutoff': 3.1}, {'cutoff': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]
