import pymcnp
from .... import _utils


class Test_Bar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Bar
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.BarBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
