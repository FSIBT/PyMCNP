import pymcnp
from .... import _utils


class Test_Refi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Refi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.RefiBuilder
        EXAMPLES_VALID = [{'refractive_index': _utils.string.type.REAL}, {'refractive_index': 3.1}, {'refractive_index': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'refractive_index': None}]
