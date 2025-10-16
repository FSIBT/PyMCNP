import pymcnp
from ... import consts
from ... import classes


class Test_F_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.F_1
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '5', 'designator': consts.string.types.DESIGNATOR, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': 5, 'designator': consts.string.types.DESIGNATOR, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': 'nd'},
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': pymcnp.types.Integer(5),
                'designator': consts.ast.types.DESIGNATOR,
                'spheres': [consts.ast.inp.f_1.SPHERE],
                'nd': pymcnp.types.String('nd'),
            },
            {'prefix': None, 'suffix': '5', 'designator': consts.string.types.DESIGNATOR, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': None, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': consts.string.types.DESIGNATOR, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': consts.string.types.DESIGNATOR, 'spheres': None, 'nd': 'nd'},
            {'prefix': 'hello', 'suffix': '5', 'designator': consts.string.types.DESIGNATOR, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '1', 'designator': consts.string.types.DESIGNATOR, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'designator': consts.string.types.DESIGNATOR, 'spheres': [consts.string.inp.f_1.SPHERE], 'nd': 'hello'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.F_1
        EXAMPLES_VALID = [consts.string.inp.F_1]
        EXAMPLES_INVALID = ['hello']
