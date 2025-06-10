import pymcnp
from ... import _utils


class Test_Za:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Za
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ZaBuilder
        EXAMPLES_VALID = [{'anything': _utils.string.type.STRING}, {'anything': _utils.ast.type.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []
