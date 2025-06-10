import pymcnp
from .... import _utils


class Test_Refs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Refs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.RefsBuilder
        EXAMPLES_VALID = [{'coefficents': [_utils.string.type.REAL]}, {'coefficents': [3.1]}, {'coefficents': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'coefficents': None}]
