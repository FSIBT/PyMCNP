import pymcnp
from ... import _utils


class Test_Fs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FsBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'numbers': [_utils.string.type.INTEGER], 't': 't', 'c': 'c'},
            {'suffix': 1, 'numbers': [1], 't': 't', 'c': 'c'},
            {'suffix': _utils.ast.type.INTEGER, 'numbers': [_utils.ast.type.INTEGER], 't': pymcnp.utils.types.String('t'), 'c': pymcnp.utils.types.String('c')},
            {'suffix': _utils.string.type.INTEGER, 'numbers': [_utils.string.type.INTEGER], 't': None, 'c': 'c'},
            {'suffix': _utils.string.type.INTEGER, 'numbers': [_utils.string.type.INTEGER], 't': 't', 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'numbers': [_utils.string.type.INTEGER], 't': 't', 'c': 'c'},
            {'suffix': _utils.string.type.INTEGER, 'numbers': None, 't': 't', 'c': 'c'},
            {'suffix': _utils.string.type.INTEGER, 'numbers': [_utils.string.type.INTEGER], 't': 'hello', 'c': 'c'},
            {'suffix': _utils.string.type.INTEGER, 'numbers': [_utils.string.type.INTEGER], 't': 't', 'c': 'hello'},
        ]
