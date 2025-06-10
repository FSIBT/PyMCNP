import pymcnp
from ... import _utils


class Test_F_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.F_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FBuilder_2
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': 5, 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {
                'prefix': pymcnp.utils.types.String('*'),
                'suffix': pymcnp.utils.types.Integer(5),
                'a': pymcnp.utils.types.String('x'),
                'designator': _utils.ast.type.DESIGNATOR,
                'rings': [_utils.ast.type.RING],
                'nd': pymcnp.utils.types.String('nd'),
            },
            {'prefix': None, 'suffix': '5', 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': None, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': None, 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': None, 'nd': 'nd'},
            {'prefix': 'hello', 'suffix': '5', 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '1', 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'hello', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': _utils.string.type.DESIGNATOR, 'rings': [_utils.string.type.RING], 'nd': 'hello'},
        ]
