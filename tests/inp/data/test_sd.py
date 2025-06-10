import pymcnp
from ... import _utils


class Test_Sd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SdBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'information': [_utils.string.type.REAL]},
            {'suffix': 1, 'information': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'information': [_utils.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'information': [_utils.string.type.REAL]}, {'suffix': _utils.string.type.INTEGER, 'information': None}]
