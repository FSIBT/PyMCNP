import pymcnp
from .... import consts
from .... import classes


class Test_F_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.F_2
        EXAMPLES_VALID = [
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': pymcnp.types.Integer(5),
                'a': pymcnp.types.String('x'),
                'designator': consts.ast.type.DESIGNATOR,
                'rings': [consts.ast.type.RING],
                'nd': pymcnp.types.String('nd'),
            },
            {
                'prefix': None,
                'suffix': pymcnp.types.Integer(5),
                'a': pymcnp.types.String('x'),
                'designator': consts.ast.type.DESIGNATOR,
                'rings': [consts.ast.type.RING],
                'nd': pymcnp.types.String('nd'),
            },
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': pymcnp.types.Integer(5),
                'a': pymcnp.types.String('x'),
                'designator': None,
                'rings': [consts.ast.type.RING],
                'nd': pymcnp.types.String('nd'),
            },
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': pymcnp.types.Integer(5),
                'a': pymcnp.types.String('x'),
                'designator': consts.ast.type.DESIGNATOR,
                'rings': [consts.ast.type.RING],
                'nd': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': None,
                'a': pymcnp.types.String('x'),
                'designator': consts.ast.type.DESIGNATOR,
                'rings': [consts.ast.type.RING],
                'nd': pymcnp.types.String('nd'),
            },
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': pymcnp.types.Integer(5),
                'a': None,
                'designator': consts.ast.type.DESIGNATOR,
                'rings': [consts.ast.type.RING],
                'nd': pymcnp.types.String('nd'),
            },
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': pymcnp.types.Integer(5),
                'a': pymcnp.types.String('x'),
                'designator': consts.ast.type.DESIGNATOR,
                'rings': None,
                'nd': pymcnp.types.String('nd'),
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.F_2
        EXAMPLES_VALID = [consts.string.inp.data.F_2]
        EXAMPLES_INVALID = ['hello']


class Test_FBuilder_2:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FBuilder_2
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': 5, 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': pymcnp.types.Integer(5),
                'a': pymcnp.types.String('x'),
                'designator': consts.ast.type.DESIGNATOR,
                'rings': [consts.ast.type.RING],
                'nd': pymcnp.types.String('nd'),
            },
            {'prefix': None, 'suffix': '5', 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': None, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': None, 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': None, 'nd': 'nd'},
            {'prefix': 'hello', 'suffix': '5', 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '1', 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'hello', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'nd'},
            {'prefix': '*', 'suffix': '5', 'a': 'x', 'designator': consts.string.type.DESIGNATOR, 'rings': [consts.string.type.RING], 'nd': 'hello'},
        ]
