import pymcnp
from ... import _utils


class Test_Pikmt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Pikmt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.PikmtBuilder
        EXAMPLES_VALID = [{'biases': [_utils.string.type.PHOTONBIAS]}, {'biases': [_utils.ast.type.PHOTONBIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]
