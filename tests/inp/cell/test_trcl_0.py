import pymcnp
from ... import _utils


class Test_Trcl_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_0
        EXAMPLES_VALID = [{'transformation': _utils.string.type.INTEGER}, {'transformation': 1}, {'transformation': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'transformation': None}]
