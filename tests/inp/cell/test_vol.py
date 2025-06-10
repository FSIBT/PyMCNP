import pymcnp
from ... import _utils


class Test_Vol:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Vol
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.VolBuilder
        EXAMPLES_VALID = [{'volume': _utils.string.type.REAL}, {'volume': 3.1}, {'volume': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'volume': None}]
