import pymcnp
from ... import _utils


class Test_Ctme:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ctme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.CtmeBuilder
        EXAMPLES_VALID = [{'tme': _utils.string.type.INTEGER}, {'tme': 1}, {'tme': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'tme': None}]
