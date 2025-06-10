import pymcnp
from .... import _utils


class Test_Thin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Thin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ThinBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
