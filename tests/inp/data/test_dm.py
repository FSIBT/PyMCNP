import pymcnp
from ... import _utils


class Test_Dm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Dm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.DmBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'zaids': [_utils.string.type.ZAID]},
            {'suffix': 1, 'zaids': [_utils.string.type.ZAID]},
            {'suffix': _utils.ast.type.INTEGER, 'zaids': [_utils.ast.type.ZAID]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'zaids': [_utils.string.type.ZAID]}, {'suffix': _utils.string.type.INTEGER, 'zaids': None}]
