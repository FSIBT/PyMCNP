import pymcnp
from ... import _utils


class Test_Trcl_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_1
        EXAMPLES_VALID = [{'transformation': _utils.string.type.TRANSFORMATION_0}, {'transformation': _utils.ast.type.TRANSFORMATION_0}]
        EXAMPLES_INVALID = [{'transformation': None}]
