import pymcnp
from .... import _utils


class Test_Tal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TalBuilder
        EXAMPLES_VALID = [{'n': _utils.string.type.INTEGER}, {'n': 1}, {'n': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]
