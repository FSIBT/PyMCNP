import pymcnp
from .... import _utils


class Test_List:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.List
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.ListBuilder
        EXAMPLES_VALID = [{'reactions': _utils.string.type.REAL}, {'reactions': 3.1}, {'reactions': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'reactions': None}]
