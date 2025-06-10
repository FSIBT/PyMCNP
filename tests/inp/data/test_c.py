import pymcnp
from ... import _utils


class Test_C:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.C
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.CBuilder
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 't': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': 1, 'bounds': [3.1], 't': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
            {'prefix': pymcnp.utils.types.String('*'), 'suffix': _utils.ast.type.INTEGER, 'bounds': [_utils.ast.type.REAL], 't': _utils.ast.type.STRING, 'c': _utils.ast.type.STRING},
            {'prefix': None, 'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 't': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 't': None, 'c': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 't': _utils.string.type.STRING, 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'bounds': [_utils.string.type.REAL], 't': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'bounds': None, 't': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
            {'prefix': 'hello', 'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 't': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
        ]
