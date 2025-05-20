import pymcnp
from .... import _utils


class Test_Iu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Iu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.df_1.IuBuilder
        EXAMPLES_VALID = [{'units': '1'}, {'units': 1}, {'units': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'units': None}]


class Test_Fac:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Fac
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.df_1.FacBuilder
        EXAMPLES_VALID = [
            {'normalization': '1'},
            {'normalization': 1},
            {'normalization': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [{'normalization': None}]


class Test_Ic:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Ic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.df_1.IcBuilder
        EXAMPLES_VALID = [
            {'function': '10'},
            {'function': 10},
            {'function': pymcnp.utils.types.Integer(10)},
        ]
        EXAMPLES_INVALID = [{'function': None}]


class Test_Log:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Log
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.df_1.LogBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Lin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Lin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.df_1.LinBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []
