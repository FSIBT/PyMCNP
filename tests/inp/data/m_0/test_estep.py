import pymcnp
from .... import _utils


class Test_Estep:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Estep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.EstepBuilder
        EXAMPLES_VALID = [{'step': _utils.string.type.INTEGER}, {'step': 1}, {'step': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'step': None}]
