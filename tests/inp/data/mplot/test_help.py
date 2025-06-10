import pymcnp
from .... import _utils


class Test_Help:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Help
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.HelpBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
