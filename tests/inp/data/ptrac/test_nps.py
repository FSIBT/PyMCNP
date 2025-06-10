import pymcnp
from .... import _utils


class Test_Nps:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.NpsBuilder
        EXAMPLES_VALID = [{'particles': [_utils.string.type.INTEGER]}, {'particles': [1]}, {'particles': [_utils.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'particles': None}]
