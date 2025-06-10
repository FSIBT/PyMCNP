import pymcnp
from .... import _utils


class Test_Hist:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Hist
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.rand.HistBuilder
        EXAMPLES_VALID = [{'hist': _utils.string.type.INTEGER}, {'hist': 1}, {'hist': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'hist': None}]
