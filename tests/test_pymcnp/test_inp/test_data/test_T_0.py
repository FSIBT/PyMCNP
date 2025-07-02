import pymcnp
from .... import consts
from .... import classes


class Test_T_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.T_0
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'bounds': [consts.ast.type.REAL], 'nt': consts.ast.type.STRING, 'c': consts.ast.type.STRING},
            {'suffix': consts.ast.type.INTEGER, 'bounds': [consts.ast.type.REAL], 'nt': None, 'c': consts.ast.type.STRING},
            {'suffix': consts.ast.type.INTEGER, 'bounds': [consts.ast.type.REAL], 'nt': consts.ast.type.STRING, 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'bounds': [consts.ast.type.REAL], 'nt': consts.ast.type.STRING, 'c': consts.ast.type.STRING},
            {'suffix': consts.ast.type.INTEGER, 'bounds': None, 'nt': consts.ast.type.STRING, 'c': consts.ast.type.STRING},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.T_0
        EXAMPLES_VALID = [consts.string.inp.data.T_0]
        EXAMPLES_INVALID = ['hello']


class Test_TBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.TBuilder_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 'nt': consts.string.type.STRING, 'c': consts.string.type.STRING},
            {'suffix': 1, 'bounds': [3.1], 'nt': consts.string.type.STRING, 'c': consts.string.type.STRING},
            {'suffix': consts.ast.type.INTEGER, 'bounds': [consts.ast.type.REAL], 'nt': consts.ast.type.STRING, 'c': consts.ast.type.STRING},
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 'nt': None, 'c': consts.string.type.STRING},
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 'nt': consts.string.type.STRING, 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'bounds': [consts.string.type.REAL], 'nt': consts.string.type.STRING, 'c': consts.string.type.STRING},
            {'suffix': consts.string.type.INTEGER, 'bounds': None, 'nt': consts.string.type.STRING, 'c': consts.string.type.STRING},
        ]
