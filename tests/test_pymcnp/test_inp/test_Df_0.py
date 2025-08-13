import pymcnp
from ... import consts
from ... import classes


class Test_Df_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Df_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'method': 'log', 'values': [consts.string.types.REAL]},
            {'suffix': 1, 'method': 'log', 'values': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'method': pymcnp.types.String('log'), 'values': [consts.ast.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'method': None, 'values': [consts.string.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'method': 'log', 'values': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'method': 'log', 'values': None},
            {'suffix': consts.string.types.INTEGER, 'method': 'hello', 'values': [consts.string.types.REAL]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Df_0
        EXAMPLES_VALID = [consts.string.inp.DF_0]
        EXAMPLES_INVALID = ['hello']
