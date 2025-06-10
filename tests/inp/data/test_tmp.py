import pymcnp
from ... import _utils


class Test_Tmp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tmp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.TmpBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'temperatures': [_utils.string.type.REAL]},
            {'suffix': 1, 'temperatures': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'temperatures': [_utils.ast.type.REAL]},
            {'suffix': None, 'temperatures': [_utils.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': _utils.string.type.INTEGER, 'temperatures': None}]
