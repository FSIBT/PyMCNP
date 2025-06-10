import pymcnp
from .... import _utils


class Test_Legend:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Legend
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LegendBuilder
        EXAMPLES_VALID = [
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL},
            {'x': 3.1, 'y': 3.1},
            {'x': _utils.ast.type.REAL, 'y': _utils.ast.type.REAL},
            {'x': None, 'y': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': None},
        ]
        EXAMPLES_INVALID = []
