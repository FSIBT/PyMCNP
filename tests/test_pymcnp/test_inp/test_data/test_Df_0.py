import pymcnp
from .... import consts
from .... import classes


class Test_Df_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Df_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'method': 'log', 'values': [consts.string.type.REAL]},
            {'suffix': 1, 'method': 'log', 'values': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'method': pymcnp.types.String('log'), 'values': [consts.ast.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'method': None, 'values': [consts.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'method': 'log', 'values': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'method': 'log', 'values': None},
            {'suffix': consts.string.type.INTEGER, 'method': 'hello', 'values': [consts.string.type.REAL]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Df_0
        EXAMPLES_VALID = [consts.string.inp.data.DF_0]
        EXAMPLES_INVALID = ['hello']
