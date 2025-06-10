import pymcnp
from .... import _utils


class Test_Dneb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dneb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.DnebBuilder
        EXAMPLES_VALID = [{'biases': [_utils.string.type.BIAS]}, {'biases': [_utils.ast.type.BIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]
