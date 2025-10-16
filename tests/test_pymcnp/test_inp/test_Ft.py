import pymcnp
from ... import consts
from ... import classes


class Test_Ft:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ft
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'treatments': consts.string.types.STRING},
            {'suffix': 1, 'treatments': consts.string.types.STRING},
            {'suffix': consts.ast.types.INTEGER, 'treatments': consts.ast.types.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'treatments': consts.string.types.STRING}, {'suffix': consts.string.types.INTEGER, 'treatments': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ft
        EXAMPLES_VALID = [consts.string.inp.FT]
        EXAMPLES_INVALID = ['hello']
