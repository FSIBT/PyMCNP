import pymcnp
from ... import consts
from ... import classes


class Test_F_3:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.F_3
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': '8', 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': consts.string.types.STRING},
            {'prefix': '*', 'suffix': 8, 'designator': consts.string.types.DESIGNATOR, 'problems': [1], 't': consts.string.types.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': pymcnp.types.Integer(8), 'designator': consts.ast.types.DESIGNATOR, 'problems': [consts.ast.types.INTEGER], 't': consts.ast.types.STRING},
            {'prefix': None, 'suffix': '8', 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': consts.string.types.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': None, 'problems': [consts.string.types.INTEGER], 't': consts.string.types.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': consts.string.types.STRING},
            {'prefix': '*', 'suffix': '8', 'designator': consts.string.types.DESIGNATOR, 'problems': None, 't': consts.string.types.STRING},
            {'prefix': 'hello', 'suffix': '8', 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': consts.string.types.STRING},
            {'prefix': '*', 'suffix': '1', 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': consts.string.types.STRING},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.F_3
        EXAMPLES_VALID = [consts.string.inp.F_3]
        EXAMPLES_INVALID = ['hello']
