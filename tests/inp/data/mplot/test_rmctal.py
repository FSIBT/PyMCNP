import pymcnp
from .... import _utils


class Test_Rmctal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Rmctal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.RmctalBuilder
        EXAMPLES_VALID = [{'filename': _utils.string.type.STRING}, {'filename': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]
