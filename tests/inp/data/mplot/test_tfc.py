import pymcnp
from .... import _utils


class Test_Tfc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tfc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TfcBuilder
        EXAMPLES_VALID = [{'x': _utils.string.type.STRING}, {'x': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'x': None}]
