import pymcnp
from ... import _utils


class Test_F_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.F_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FBuilder_1
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '5', 'designator': _utils.string.type.DESIGNATOR, 'spheres': [_utils.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': 5, 'designator': _utils.string.type.DESIGNATOR, 'spheres': [_utils.string.type.SPHERE], 'nd': 'nd'},
            {
                'prefix': pymcnp.utils.types.String('*'),
                'suffix': pymcnp.utils.types.Integer(5),
                'designator': _utils.ast.type.DESIGNATOR,
                'spheres': [_utils.ast.type.SPHERE],
                'nd': pymcnp.utils.types.String('nd'),
            },
            {'prefix': None, 'suffix': '5', 'designator': _utils.string.type.DESIGNATOR, 'spheres': [_utils.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': None, 'spheres': [_utils.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': _utils.string.type.DESIGNATOR, 'spheres': [_utils.string.type.SPHERE], 'nd': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': _utils.string.type.DESIGNATOR, 'spheres': [_utils.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': _utils.string.type.DESIGNATOR, 'spheres': None, 'nd': 'nd'},
            {'prefix': 'hello', 'suffix': '5', 'designator': _utils.string.type.DESIGNATOR, 'spheres': [_utils.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '1', 'designator': _utils.string.type.DESIGNATOR, 'spheres': [_utils.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': _utils.string.type.DESIGNATOR, 'spheres': [_utils.string.type.SPHERE], 'nd': 'hello'},
        ]
