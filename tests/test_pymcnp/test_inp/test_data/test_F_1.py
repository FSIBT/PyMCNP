import pymcnp
from .... import consts
from .... import classes


class Test_F_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.F_1
        EXAMPLES_VALID = [
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(5), 'designator': consts.ast.type.DESIGNATOR, 'spheres': [consts.ast.type.SPHERE], 'nd': pymcnp.types.String('nd')},
            {'prefix': None, 'suffix': pymcnp.types.Integer(5), 'designator': consts.ast.type.DESIGNATOR, 'spheres': [consts.ast.type.SPHERE], 'nd': pymcnp.types.String('nd')},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(5), 'designator': None, 'spheres': [consts.ast.type.SPHERE], 'nd': pymcnp.types.String('nd')},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(5), 'designator': consts.ast.type.DESIGNATOR, 'spheres': [consts.ast.type.SPHERE], 'nd': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': pymcnp.types.String('*'), 'suffix': None, 'designator': consts.ast.type.DESIGNATOR, 'spheres': [consts.ast.type.SPHERE], 'nd': pymcnp.types.String('nd')},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(5), 'designator': consts.ast.type.DESIGNATOR, 'spheres': None, 'nd': pymcnp.types.String('nd')},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.F_1
        EXAMPLES_VALID = [consts.string.inp.data.F_1]
        EXAMPLES_INVALID = ['hello']


class Test_FBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FBuilder_1
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '5', 'designator': consts.string.type.DESIGNATOR, 'spheres': [consts.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': 5, 'designator': consts.string.type.DESIGNATOR, 'spheres': [consts.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(5), 'designator': consts.ast.type.DESIGNATOR, 'spheres': [consts.ast.type.SPHERE], 'nd': pymcnp.types.String('nd')},
            {'prefix': None, 'suffix': '5', 'designator': consts.string.type.DESIGNATOR, 'spheres': [consts.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': None, 'spheres': [consts.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': consts.string.type.DESIGNATOR, 'spheres': [consts.string.type.SPHERE], 'nd': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'spheres': [consts.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': consts.string.type.DESIGNATOR, 'spheres': None, 'nd': 'nd'},
            {'prefix': 'hello', 'suffix': '5', 'designator': consts.string.type.DESIGNATOR, 'spheres': [consts.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '1', 'designator': consts.string.type.DESIGNATOR, 'spheres': [consts.string.type.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': consts.string.type.DESIGNATOR, 'spheres': [consts.string.type.SPHERE], 'nd': 'hello'},
        ]
