import pymcnp
from .... import _utils


class Test_Watt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Watt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.WattBuilder
        EXAMPLES_VALID = [{'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL}, {'a': 3.1, 'b': 3.1}, {'a': _utils.ast.type.REAL, 'b': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'a': None, 'b': _utils.string.type.REAL}, {'a': _utils.string.type.REAL, 'b': None}]
