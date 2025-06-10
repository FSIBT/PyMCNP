import pymcnp
from .... import _utils


class Test_Csub:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Csub
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.CsubBuilder
        EXAMPLES_VALID = [{'count': _utils.string.type.INTEGER}, {'count': 1}, {'count': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]
