import pymcnp
from .... import _utils


class Test_Pecut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Pecut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.PecutBuilder
        EXAMPLES_VALID = [{'cutoff': _utils.string.type.REAL}, {'cutoff': 3.1}, {'cutoff': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]
