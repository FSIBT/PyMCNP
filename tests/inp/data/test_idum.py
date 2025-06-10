import pymcnp
from ... import _utils


class Test_Idum:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Idum
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.IdumBuilder
        EXAMPLES_VALID = [{'intergers': [_utils.string.type.INTEGER]}, {'intergers': [1]}, {'intergers': [_utils.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'intergers': None}]
