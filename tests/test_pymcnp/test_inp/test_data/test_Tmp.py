import pymcnp
from .... import consts
from .... import classes


class Test_Tmp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Tmp
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'temperatures': [consts.string.type.REAL]},
            {'suffix': 1, 'temperatures': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'temperatures': [consts.ast.type.REAL]},
            {'suffix': None, 'temperatures': [consts.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': consts.string.type.INTEGER, 'temperatures': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Tmp
        EXAMPLES_VALID = [consts.string.inp.data.TMP]
        EXAMPLES_INVALID = ['hello']
