import pymcnp
from ... import _utils


class Test_Thtme:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Thtme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ThtmeBuilder
        EXAMPLES_VALID = [{'times': [_utils.string.type.REAL]}, {'times': [3.1]}, {'times': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'times': None}]
