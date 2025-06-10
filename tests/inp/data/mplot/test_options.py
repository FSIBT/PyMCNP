import pymcnp
from .... import _utils


class Test_Options:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Options
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.OptionsBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
