import pymcnp
from ... import consts
from ... import classes


class Test_F_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.F_2
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': 5, 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': pymcnp.types.Integer(5),
                'a': pymcnp.types.String('x'),
                'designator': consts.ast.types.DESIGNATOR,
                'rings': [consts.ast.inp.f_2.RING],
                'nd': pymcnp.types.String('nd'),
            },
            {'prefix': None, 'suffix': '5', 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': None, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': None, 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': None, 'nd': 'nd'},
            {'prefix': 'hello', 'suffix': '5', 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '1', 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'hello', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': consts.string.types.DESIGNATOR, 'rings': [consts.string.inp.f_2.RING], 'nd': 'hello'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.F_2
        EXAMPLES_VALID = [consts.string.inp.F_2]
        EXAMPLES_INVALID = ['hello']
