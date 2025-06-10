import pymcnp
from ... import _utils


class Test_Nonu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Nonu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.NonuBuilder
        EXAMPLES_VALID = [{'setting': _utils.string.type.INTEGER}, {'setting': 1}, {'setting': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
