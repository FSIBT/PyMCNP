import pymcnp
from ... import _utils


class Test_Pwt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Pwt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.PwtBuilder
        EXAMPLES_VALID = [{'weights': [_utils.string.type.REAL]}, {'weights': [3.1]}, {'weights': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'weights': None}]
