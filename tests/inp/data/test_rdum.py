import pymcnp
from ... import _utils


class Test_Rdum:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Rdum
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.RdumBuilder
        EXAMPLES_VALID = [{'floats': [_utils.string.type.REAL]}, {'floats': [3.1]}, {'floats': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'floats': None}]
