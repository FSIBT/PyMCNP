import pymcnp
from .... import consts
from .... import classes


class Test_C:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.C
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 't': consts.string.type.STRING, 'c': consts.string.type.STRING},
            {'prefix': '*', 'suffix': 1, 'bounds': [3.1], 't': consts.string.type.STRING, 'c': consts.string.type.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.type.INTEGER, 'bounds': [consts.ast.type.REAL], 't': consts.ast.type.STRING, 'c': consts.ast.type.STRING},
            {'prefix': None, 'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 't': consts.string.type.STRING, 'c': consts.string.type.STRING},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 't': None, 'c': consts.string.type.STRING},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 't': consts.string.type.STRING, 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'bounds': [consts.string.type.REAL], 't': consts.string.type.STRING, 'c': consts.string.type.STRING},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'bounds': None, 't': consts.string.type.STRING, 'c': consts.string.type.STRING},
            {'prefix': 'hello', 'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 't': consts.string.type.STRING, 'c': consts.string.type.STRING},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.C
        EXAMPLES_VALID = [consts.string.inp.data.C]
        EXAMPLES_INVALID = ['hello']
