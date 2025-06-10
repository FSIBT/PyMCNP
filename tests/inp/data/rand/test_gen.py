import pymcnp
from .... import _utils


class Test_Gen:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Gen
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.rand.GenBuilder
        EXAMPLES_VALID = [{'setting': _utils.string.type.INTEGER}, {'setting': 1}, {'setting': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
