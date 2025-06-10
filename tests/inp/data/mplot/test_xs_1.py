import pymcnp
from .... import _utils


class Test_Xs_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XsBuilder_1
        EXAMPLES_VALID = [{'m': _utils.string.type.ZAID}, {'m': _utils.ast.type.ZAID}]
        EXAMPLES_INVALID = [{'m': None}]
