import pymcnp
from ... import _utils


class Test_Ds_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ds_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.DsBuilder_0
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'option': 'h', 'js': [_utils.string.type.REAL]},
            {'suffix': 1, 'option': 'h', 'js': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'option': pymcnp.utils.types.String('h'), 'js': [_utils.ast.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'option': None, 'js': [_utils.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'h', 'js': [_utils.string.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'option': 'h', 'js': None},
            {'suffix': _utils.string.type.INTEGER, 'option': 'hello', 'js': [_utils.string.type.REAL]},
        ]
