import pymcnp
from .... import _utils


class Test_Stride:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Stride
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.rand.StrideBuilder
        EXAMPLES_VALID = [{'stride': _utils.string.type.INTEGER}, {'stride': 1}, {'stride': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'stride': None}]
