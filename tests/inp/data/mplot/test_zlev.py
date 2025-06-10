import pymcnp
from .... import _utils


class Test_Zlev:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Zlev
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ZlevBuilder
        EXAMPLES_VALID = [{'n': [_utils.string.type.STRING]}, {'n': [_utils.ast.type.STRING]}]
        EXAMPLES_INVALID = [{'n': None}]
