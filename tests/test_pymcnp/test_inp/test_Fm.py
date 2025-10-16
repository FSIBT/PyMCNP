import pymcnp
from ... import consts
from ... import classes


class Test_Fm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Fm
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'bins': consts.string.types.STRING},
            {'prefix': '*', 'suffix': 1, 'bins': consts.string.types.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.types.INTEGER, 'bins': consts.ast.types.STRING},
            {'prefix': None, 'suffix': consts.string.types.INTEGER, 'bins': consts.string.types.STRING},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'bins': consts.string.types.STRING},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'bins': None},
            {'prefix': 'hello', 'suffix': consts.string.types.INTEGER, 'bins': consts.string.types.STRING},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Fm
        EXAMPLES_VALID = [consts.string.inp.FM]
        EXAMPLES_INVALID = ['hello']
