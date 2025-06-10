import pymcnp
from ... import _utils


class Test_T_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.T_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.TBuilder_0
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 'nt': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
            {'suffix': 1, 'bounds': [3.1], 'nt': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
            {'suffix': _utils.ast.type.INTEGER, 'bounds': [_utils.ast.type.REAL], 'nt': _utils.ast.type.STRING, 'c': _utils.ast.type.STRING},
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 'nt': None, 'c': _utils.string.type.STRING},
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 'nt': _utils.string.type.STRING, 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'bounds': [_utils.string.type.REAL], 'nt': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
            {'suffix': _utils.string.type.INTEGER, 'bounds': None, 'nt': _utils.string.type.STRING, 'c': _utils.string.type.STRING},
        ]
