import pymcnp
from ... import _utils


class Test_Nonu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Nonu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.NonuBuilder
        EXAMPLES_VALID = [{'settings': [_utils.string.type.INTEGER]}, {'settings': [1]}, {'settings': [_utils.ast.type.INTEGER]}, {'settings': None}]
        EXAMPLES_INVALID = []
