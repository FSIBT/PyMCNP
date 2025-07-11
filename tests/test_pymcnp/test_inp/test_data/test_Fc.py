import pymcnp
from .... import consts
from .... import classes


class Test_Fc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Fc
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'info': consts.string.type.STRING},
            {'suffix': 1, 'info': consts.string.type.STRING},
            {'suffix': consts.ast.type.INTEGER, 'info': consts.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'info': consts.string.type.STRING}, {'suffix': consts.string.type.INTEGER, 'info': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Fc
        EXAMPLES_VALID = [consts.string.inp.data.FC]
        EXAMPLES_INVALID = ['hello']
