import pymcnp
from ... import _utils


class Test_Embdf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embdf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.EmbdfBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'multipliers': [_utils.string.type.REAL]},
            {'suffix': 1, 'multipliers': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'multipliers': [_utils.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'multipliers': [_utils.string.type.REAL]}, {'suffix': _utils.string.type.INTEGER, 'multipliers': None}]
