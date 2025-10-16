import pymcnp
from ... import consts
from ... import classes


class Test_C:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.C
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 't': consts.string.types.STRING, 'c': consts.string.types.STRING},
            {'prefix': '*', 'suffix': 1, 'bounds': [3.1], 't': consts.string.types.STRING, 'c': consts.string.types.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.types.INTEGER, 'bounds': [consts.ast.types.REAL], 't': consts.ast.types.STRING, 'c': consts.ast.types.STRING},
            {'prefix': None, 'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 't': consts.string.types.STRING, 'c': consts.string.types.STRING},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 't': None, 'c': consts.string.types.STRING},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 't': consts.string.types.STRING, 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'bounds': [consts.string.types.REAL], 't': consts.string.types.STRING, 'c': consts.string.types.STRING},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'bounds': None, 't': consts.string.types.STRING, 'c': consts.string.types.STRING},
            {'prefix': 'hello', 'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 't': consts.string.types.STRING, 'c': consts.string.types.STRING},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.C
        EXAMPLES_VALID = [consts.string.inp.C]
        EXAMPLES_INVALID = ['hello']
