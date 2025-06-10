import pymcnp
from .... import _utils


class Test_Xs_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XsBuilder_0
        EXAMPLES_VALID = [{'m': _utils.string.type.INTEGER}, {'m': 1}, {'m': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'m': None}]
