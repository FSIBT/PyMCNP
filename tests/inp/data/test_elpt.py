import pymcnp
from ... import _utils


class Test_Elpt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Elpt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ElptBuilder
        EXAMPLES_VALID = [{'cutoffs': [_utils.string.type.REAL]}, {'cutoffs': [3.1]}, {'cutoffs': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'cutoffs': None}]
