import pymcnp
from ... import consts
from ... import classes


class Test_Dm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Dm
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'zaids': [consts.string.types.ZAID]},
            {'suffix': 1, 'zaids': [consts.string.types.ZAID]},
            {'suffix': consts.ast.types.INTEGER, 'zaids': [consts.ast.types.ZAID]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'zaids': [consts.string.types.ZAID]}, {'suffix': consts.string.types.INTEGER, 'zaids': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Dm
        EXAMPLES_VALID = [consts.string.inp.DM]
        EXAMPLES_INVALID = ['hello']
