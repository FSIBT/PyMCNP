import pymcnp
from ... import _utils


class Test_Trcl_4:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_4
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_4
        EXAMPLES_VALID = [{'transformation': _utils.string.type.TRANSFORMATION_3}, {'transformation': _utils.ast.type.TRANSFORMATION_3}]
        EXAMPLES_INVALID = [{'transformation': None}]
