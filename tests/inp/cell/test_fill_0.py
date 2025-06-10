import pymcnp
from ... import _utils


class Test_Fill_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_0
        EXAMPLES_VALID = [
            {'prefix': '*', 'i': _utils.string.type.INDEX, 'j': _utils.string.type.INDEX, 'k': _utils.string.type.INDEX, 'universes': [_utils.string.type.INTEGER], 'm': _utils.string.type.INTEGER},
            {'prefix': '*', 'i': _utils.string.type.INDEX, 'j': _utils.string.type.INDEX, 'k': _utils.string.type.INDEX, 'universes': [1], 'm': 1},
            {
                'prefix': pymcnp.utils.types.String('*'),
                'i': _utils.ast.type.INDEX,
                'j': _utils.ast.type.INDEX,
                'k': _utils.ast.type.INDEX,
                'universes': [_utils.ast.type.INTEGER],
                'm': _utils.ast.type.INTEGER,
            },
            {'prefix': None, 'i': _utils.string.type.INDEX, 'j': _utils.string.type.INDEX, 'k': _utils.string.type.INDEX, 'universes': [_utils.string.type.INTEGER], 'm': _utils.string.type.INTEGER},
            {'prefix': '*', 'i': _utils.string.type.INDEX, 'j': _utils.string.type.INDEX, 'k': _utils.string.type.INDEX, 'universes': [_utils.string.type.INTEGER], 'm': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'i': None, 'j': _utils.string.type.INDEX, 'k': _utils.string.type.INDEX, 'universes': [_utils.string.type.INTEGER], 'm': _utils.string.type.INTEGER},
            {'prefix': '*', 'i': _utils.string.type.INDEX, 'j': None, 'k': _utils.string.type.INDEX, 'universes': [_utils.string.type.INTEGER], 'm': _utils.string.type.INTEGER},
            {'prefix': '*', 'i': _utils.string.type.INDEX, 'j': _utils.string.type.INDEX, 'k': None, 'universes': [_utils.string.type.INTEGER], 'm': _utils.string.type.INTEGER},
            {'prefix': '*', 'i': _utils.string.type.INDEX, 'j': _utils.string.type.INDEX, 'k': _utils.string.type.INDEX, 'universes': None, 'm': _utils.string.type.INTEGER},
            {
                'prefix': 'hello',
                'i': _utils.string.type.INDEX,
                'j': _utils.string.type.INDEX,
                'k': _utils.string.type.INDEX,
                'universes': [_utils.string.type.INTEGER],
                'm': _utils.string.type.INTEGER,
            },
        ]
