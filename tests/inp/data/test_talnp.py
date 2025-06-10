import pymcnp
from ... import _utils


class Test_Talnp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Talnp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.TalnpBuilder
        EXAMPLES_VALID = [{'tallies': [_utils.string.type.INTEGER]}, {'tallies': [1]}, {'tallies': [_utils.ast.type.INTEGER]}, {'tallies': None}]
        EXAMPLES_INVALID = []
