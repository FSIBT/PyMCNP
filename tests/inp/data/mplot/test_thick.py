import pymcnp
from .... import _utils


class Test_Thick:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Thick
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ThickBuilder
        EXAMPLES_VALID = [{'x': _utils.string.type.REAL}, {'x': 3.1}, {'x': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'x': None}]
