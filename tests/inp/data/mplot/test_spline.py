import pymcnp
from .... import _utils


class Test_Spline:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Spline
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.SplineBuilder
        EXAMPLES_VALID = [{'x': _utils.string.type.REAL}, {'x': 3.1}, {'x': _utils.ast.type.REAL}, {'x': None}]
        EXAMPLES_INVALID = []
