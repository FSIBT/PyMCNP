import pymcnp
from .... import _utils


class Test_Max:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Max
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.MaxBuilder
        EXAMPLES_VALID = [{'events': _utils.string.type.INTEGER}, {'events': 1}, {'events': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'events': None}]
