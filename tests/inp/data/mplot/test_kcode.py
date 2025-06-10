import pymcnp
from .... import _utils


class Test_Kcode:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Kcode
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.KcodeBuilder
        EXAMPLES_VALID = [{'i': _utils.string.type.INTEGER}, {'i': 1}, {'i': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'i': None}]
