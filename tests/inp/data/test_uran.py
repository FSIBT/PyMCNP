import pymcnp
from ... import _utils


class Test_Uran:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Uran
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.UranBuilder
        EXAMPLES_VALID = [{'transformations': [_utils.string.type.STOCHASTIC]}, {'transformations': [_utils.ast.type.STOCHASTIC]}]
        EXAMPLES_INVALID = [{'transformations': None}]
