import pymcnp
from ... import _utils


class Test_F_3:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.F_3
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FBuilder_3
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '8', 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': 8, 'designator': _utils.string.type.DESIGNATOR, 'problems': [1], 't': _utils.string.type.STRING},
            {
                'prefix': pymcnp.utils.types.String('*'),
                'suffix': pymcnp.utils.types.Integer(8),
                'designator': _utils.ast.type.DESIGNATOR,
                'problems': [_utils.ast.type.INTEGER],
                't': _utils.ast.type.STRING,
            },
            {'prefix': None, 'suffix': '8', 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': None, 'problems': [_utils.string.type.INTEGER], 't': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': _utils.string.type.DESIGNATOR, 'problems': None, 't': _utils.string.type.STRING},
            {'prefix': 'hello', 'suffix': '8', 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': '1', 'designator': _utils.string.type.DESIGNATOR, 'problems': [_utils.string.type.INTEGER], 't': _utils.string.type.STRING},
        ]
