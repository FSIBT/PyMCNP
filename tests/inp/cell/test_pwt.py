import pymcnp
from ... import _utils


class Test_Pwt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Pwt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.PwtBuilder
        EXAMPLES_VALID = [{'weight': _utils.string.type.REAL}, {'weight': 3.1}, {'weight': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'weight': None}]
