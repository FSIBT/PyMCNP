import pymcnp
from ... import _utils


class Test_Sb_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sb_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SbBuilder_0
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'option': 'd', 'biases': [_utils.string.type.REAL]},
            {'suffix': 1, 'option': 'd', 'biases': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'option': pymcnp.utils.types.String('d'), 'biases': [_utils.ast.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'option': None, 'biases': [_utils.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'd', 'biases': [_utils.string.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'option': 'd', 'biases': None},
            {'suffix': _utils.string.type.INTEGER, 'option': 'hello', 'biases': [_utils.string.type.REAL]},
        ]
