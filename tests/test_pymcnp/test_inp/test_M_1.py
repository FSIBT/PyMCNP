import pymcnp
from ... import consts
from ... import classes


class Test_M_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.M_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'abx': consts.string.types.STRING},
            {'suffix': 1, 'abx': consts.string.types.STRING},
            {'suffix': consts.ast.types.INTEGER, 'abx': consts.ast.types.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'abx': consts.string.types.STRING}, {'suffix': consts.string.types.INTEGER, 'abx': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.M_1
        EXAMPLES_VALID = [consts.string.inp.M_1]
        EXAMPLES_INVALID = ['hello']
