import pymcnp
from .... import _utils


class Test_Nonorm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Nonorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.NonormBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
