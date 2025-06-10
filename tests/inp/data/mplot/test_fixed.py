import pymcnp
from .... import _utils


class Test_Fixed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Fixed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FixedBuilder
        EXAMPLES_VALID = [{'q': 't', 'n': _utils.string.type.INTEGER}, {'q': 't', 'n': 1}, {'q': pymcnp.utils.types.String('t'), 'n': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'q': None, 'n': _utils.string.type.INTEGER}, {'q': 't', 'n': None}, {'q': 'hello', 'n': _utils.string.type.INTEGER}]
