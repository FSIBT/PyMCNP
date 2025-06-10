import pymcnp
from ... import _utils


class Test_Sp_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sp_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SpBuilder_0
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'option': 'd', 'probabilities': [_utils.string.type.REAL]},
            {'suffix': 1, 'option': 'd', 'probabilities': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'option': pymcnp.utils.types.String('d'), 'probabilities': [_utils.ast.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'option': None, 'probabilities': [_utils.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'd', 'probabilities': [_utils.string.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'option': 'd', 'probabilities': None},
            {'suffix': _utils.string.type.INTEGER, 'option': 'hello', 'probabilities': [_utils.string.type.REAL]},
        ]
