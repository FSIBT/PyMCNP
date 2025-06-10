import pymcnp
from ... import _utils


class Test_F_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.F_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FBuilder_0
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': 1, 'designator': _utils.string.type.DESIGNATOR, 'problems': [1], 't': 't'},
            {
                'prefix': pymcnp.utils.types.String('*'),
                'suffix': _utils.ast.type.INTEGER,
                'designator': _utils.ast.type.DESIGNATOR,
                'problems': [_utils.ast.type.INTEGER],
                't': pymcnp.utils.types.String('t'),
            },
            {'prefix': None, 'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'designator': None, 'problems': [_utils.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'problems': None, 't': 't'},
            {'prefix': 'hello', 'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': 'hello'},
        ]
