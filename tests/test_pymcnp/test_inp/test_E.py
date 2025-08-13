import pymcnp
from ... import consts
from ... import classes


class Test_E:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.E
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 'nt': consts.string.types.STRING, 'c': consts.string.types.STRING},
            {'suffix': 1, 'bounds': [3.1], 'nt': consts.string.types.STRING, 'c': consts.string.types.STRING},
            {'suffix': consts.ast.types.INTEGER, 'bounds': [consts.ast.types.REAL], 'nt': consts.ast.types.STRING, 'c': consts.ast.types.STRING},
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 'nt': None, 'c': consts.string.types.STRING},
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 'nt': consts.string.types.STRING, 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'bounds': [consts.string.types.REAL], 'nt': consts.string.types.STRING, 'c': consts.string.types.STRING},
            {'suffix': consts.string.types.INTEGER, 'bounds': None, 'nt': consts.string.types.STRING, 'c': consts.string.types.STRING},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.E
        EXAMPLES_VALID = [consts.string.inp.E]
        EXAMPLES_INVALID = ['hello']
