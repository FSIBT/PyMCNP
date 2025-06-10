import pymcnp
from ..... import _utils


class Test_Log:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Log
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.LogBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
