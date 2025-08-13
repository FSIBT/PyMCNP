import pymcnp
from ... import consts
from ... import classes


class Test_Tmp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Tmp
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'temperatures': [consts.string.types.REAL]},
            {'suffix': 1, 'temperatures': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'temperatures': [consts.ast.types.REAL]},
            {'suffix': None, 'temperatures': [consts.string.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': consts.string.types.INTEGER, 'temperatures': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Tmp
        EXAMPLES_VALID = [consts.string.inp.TMP]
        EXAMPLES_INVALID = ['hello']
