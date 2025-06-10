import pymcnp
from ... import _utils


class Test_Mplot:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mplot
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.MplotBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.mplot.BAR]}, {'options': [_utils.builder.inp.data.mplot.BAR]}, {'options': [_utils.ast.inp.data.mplot.BAR]}, {'options': None}]
        EXAMPLES_INVALID = []
