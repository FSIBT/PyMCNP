import pymcnp
from ... import _utils


class Test_Fu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FuBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 'nt': 'nt', 'c': 'c'},
            {'suffix': 1, 'bounds': [3.1], 'nt': 'nt', 'c': 'c'},
            {'suffix': _utils.ast.type.INTEGER, 'bounds': [_utils.ast.type.REAL], 'nt': pymcnp.utils.types.String('nt'), 'c': pymcnp.utils.types.String('c')},
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 'nt': None, 'c': 'c'},
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 'nt': 'nt', 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'bounds': [_utils.string.type.REAL], 'nt': 'nt', 'c': 'c'},
            {'suffix': _utils.string.type.INTEGER, 'bounds': None, 'nt': 'nt', 'c': 'c'},
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 'nt': 'hello', 'c': 'c'},
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL], 'nt': 'nt', 'c': 'hello'},
        ]
