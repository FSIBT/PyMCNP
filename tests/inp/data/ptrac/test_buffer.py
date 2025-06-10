import pymcnp
from .... import _utils


class Test_Buffer:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Buffer
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.BufferBuilder
        EXAMPLES_VALID = [{'storage': _utils.string.type.INTEGER}, {'storage': 1}, {'storage': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'storage': None}]
