import pymcnp
from ... import _utils


class Test_Bflcl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Bflcl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.BflclBuilder
        EXAMPLES_VALID = [{'number': _utils.string.type.INTEGER}, {'number': 1}, {'number': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]
