import pymcnp
from ..... import _utils


class Test_All:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.All
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.AllBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
