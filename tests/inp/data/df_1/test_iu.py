import pymcnp
from .... import _utils


class Test_Iu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Iu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.df_1.IuBuilder
        EXAMPLES_VALID = [{'units': _utils.string.type.INTEGER}, {'units': 1}, {'units': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'units': None}]
