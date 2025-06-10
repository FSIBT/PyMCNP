import pymcnp
from .... import _utils


class Test_Meph:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Meph
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.MephBuilder
        EXAMPLES_VALID = [{'events': _utils.string.type.INTEGER}, {'events': 1}, {'events': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'events': None}]
