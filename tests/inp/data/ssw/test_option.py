import pymcnp
from .... import _utils


class Test_Sym:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssw.Sym
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssw.SymBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Pty:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssw.Pty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssw.PtyBuilder
        EXAMPLES_VALID = [{'tracks': ['n']}, {'tracks': [_utils.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'tracks': None}]


class Test_Cel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssw.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssw.CelBuilder
        EXAMPLES_VALID = [{'cfs': ['1']}, {'cfs': [1]}, {'cfs': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'cfs': None}]
