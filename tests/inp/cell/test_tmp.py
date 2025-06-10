import pymcnp
from ... import _utils


class Test_Tmp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Tmp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TmpBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'temperature': [_utils.string.type.REAL]},
            {'suffix': 1, 'temperature': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'temperature': [_utils.ast.type.REAL]},
            {'suffix': None, 'temperature': [_utils.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': _utils.string.type.INTEGER, 'temperature': None}]
