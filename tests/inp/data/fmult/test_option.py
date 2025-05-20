import pymcnp
from .... import _utils


class Test_Sfnu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Sfnu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.SfnuBuilder
        EXAMPLES_VALID = [
            {'distribution': ['1.0']},
            {'distribution': [1.0]},
            {'distribution': [_utils.REAL]},
        ]
        EXAMPLES_INVALID = [{'distribution': None}]


class Test_Width:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Width
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.WidthBuilder
        EXAMPLES_VALID = [{'width': '1.0'}, {'width': 1.0}, {'width': _utils.REAL}]
        EXAMPLES_INVALID = [{'width': None}]


class Test_Sfyield:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Sfyield
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.SfyieldBuilder
        EXAMPLES_VALID = [
            {'fission_yield': '1.0'},
            {'fission_yield': 1.0},
            {'fission_yield': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'fission_yield': None}]


class Test_Watt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Watt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.WattBuilder
        EXAMPLES_VALID = [
            {'a': '1.0', 'b': '1.0'},
            {'a': 1.0, 'b': 1.0},
            {'a': _utils.REAL, 'b': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'a': None, 'b': '1.0'}, {'a': '1.0', 'b': None}]


class Test_Method:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Method
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.MethodBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Data:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Data
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.DataBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Shift:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Shift
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.ShiftBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
