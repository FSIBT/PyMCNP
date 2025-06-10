import pymcnp
from .... import _utils


class Test_Fac:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Fac
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.df_1.FacBuilder
        EXAMPLES_VALID = [{'normalization': _utils.string.type.INTEGER}, {'normalization': 1}, {'normalization': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'normalization': None}]
