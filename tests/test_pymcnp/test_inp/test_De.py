import pymcnp
from ... import consts
from ... import classes


class Test_De:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.De
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
        element = pymcnp.inp.De
        EXAMPLES_VALID = [consts.string.inp.DE]
        EXAMPLES_INVALID = ['hello']
