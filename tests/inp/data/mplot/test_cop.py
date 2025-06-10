import pymcnp
from .... import _utils


class Test_Cop:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Cop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.CopBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
