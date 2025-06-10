import pymcnp
from ... import _utils


class Test_Rand:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Rand
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.RandBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.rand.GEN]}, {'options': [_utils.builder.inp.data.rand.GEN]}, {'options': [_utils.ast.inp.data.rand.GEN]}, {'options': None}]
        EXAMPLES_INVALID = []
