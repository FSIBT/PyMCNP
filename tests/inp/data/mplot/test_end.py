import pymcnp
from .... import _utils


class Test_End:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.End
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.EndBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
