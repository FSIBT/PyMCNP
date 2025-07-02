import pymcnp
from .... import consts
from .... import classes


class Test_M_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.M_1
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'abx': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'suffix': None, 'abx': consts.ast.type.STRING}, {'suffix': consts.ast.type.INTEGER, 'abx': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.M_1
        EXAMPLES_VALID = [consts.string.inp.data.M_1]
        EXAMPLES_INVALID = ['hello']


class Test_MBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.MBuilder_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'abx': consts.string.type.STRING},
            {'suffix': 1, 'abx': consts.string.type.STRING},
            {'suffix': consts.ast.type.INTEGER, 'abx': consts.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'abx': consts.string.type.STRING}, {'suffix': consts.string.type.INTEGER, 'abx': None}]
