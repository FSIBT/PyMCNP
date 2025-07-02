import pymcnp
from .... import consts
from .... import classes


class Test_F_3:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.F_3
        EXAMPLES_VALID = [
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(8), 'designator': consts.ast.type.DESIGNATOR, 'problems': [consts.ast.type.INTEGER], 't': consts.ast.type.STRING},
            {'prefix': None, 'suffix': pymcnp.types.Integer(8), 'designator': consts.ast.type.DESIGNATOR, 'problems': [consts.ast.type.INTEGER], 't': consts.ast.type.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(8), 'designator': None, 'problems': [consts.ast.type.INTEGER], 't': consts.ast.type.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(8), 'designator': consts.ast.type.DESIGNATOR, 'problems': [consts.ast.type.INTEGER], 't': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': pymcnp.types.String('*'), 'suffix': None, 'designator': consts.ast.type.DESIGNATOR, 'problems': [consts.ast.type.INTEGER], 't': consts.ast.type.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(8), 'designator': consts.ast.type.DESIGNATOR, 'problems': None, 't': consts.ast.type.STRING},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.F_3
        EXAMPLES_VALID = [consts.string.inp.data.F_3]
        EXAMPLES_INVALID = ['hello']


class Test_FBuilder_3:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FBuilder_3
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '8', 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': consts.string.type.STRING},
            {'prefix': '*', 'suffix': 8, 'designator': consts.string.type.DESIGNATOR, 'problems': [1], 't': consts.string.type.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(8), 'designator': consts.ast.type.DESIGNATOR, 'problems': [consts.ast.type.INTEGER], 't': consts.ast.type.STRING},
            {'prefix': None, 'suffix': '8', 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': consts.string.type.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': None, 'problems': [consts.string.type.INTEGER], 't': consts.string.type.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': consts.string.type.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': consts.string.type.DESIGNATOR, 'problems': None, 't': consts.string.type.STRING},
            {'prefix': 'hello', 'suffix': '8', 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': consts.string.type.STRING},
            {'prefix': '*', 'suffix': '1', 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': consts.string.type.STRING},
        ]
