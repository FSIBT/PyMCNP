import pymcnp
from .... import _utils


class Test_Slib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Slib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.SlibBuilder
        EXAMPLES_VALID = [{'abx': _utils.string.type.STRING}, {'abx': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'abx': None}]
