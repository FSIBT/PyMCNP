import pymcnp
from ... import consts
from ... import classes


class Test_Fc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Fc
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'info': consts.string.types.STRING},
            {'suffix': 1, 'info': consts.string.types.STRING},
            {'suffix': consts.ast.types.INTEGER, 'info': consts.ast.types.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'info': consts.string.types.STRING}, {'suffix': consts.string.types.INTEGER, 'info': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Fc
        EXAMPLES_VALID = [consts.string.inp.FC]
        EXAMPLES_INVALID = ['hello']
