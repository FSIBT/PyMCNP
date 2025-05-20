import pymcnp
from .... import _utils


class Test_Cbeg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cbeg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.CbegBuilder
        EXAMPLES_VALID = [{'time': '1.0'}, {'time': 1.0}, {'time': _utils.REAL}]
        EXAMPLES_INVALID = [{'time': None}]


class Test_Cfrq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cfrq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.CfrqBuilder
        EXAMPLES_VALID = [{'frequency': '1.0'}, {'frequency': 1.0}, {'frequency': _utils.REAL}]
        EXAMPLES_INVALID = [{'frequency': None}]


class Test_Cofi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cofi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.CofiBuilder
        EXAMPLES_VALID = [{'time': '1.0'}, {'time': 1.0}, {'time': _utils.REAL}]
        EXAMPLES_INVALID = [{'time': None}]


class Test_Coni:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Coni
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.ConiBuilder
        EXAMPLES_VALID = [{'time': '1.0'}, {'time': 1.0}, {'time': _utils.REAL}]
        EXAMPLES_INVALID = [{'time': None}]


class Test_Csub:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Csub
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.CsubBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Cend:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cend
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.t_1.CendBuilder
        EXAMPLES_VALID = [{'time': '1.0'}, {'time': 1.0}, {'time': _utils.REAL}]
        EXAMPLES_INVALID = [{'time': None}]
