import pymcnp
from ... import consts
from ... import classes


class Test_Tm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Tm
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'multipliers': [consts.string.types.REAL]},
            {'suffix': 1, 'multipliers': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'multipliers': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'multipliers': [consts.string.types.REAL]}, {'suffix': consts.string.types.INTEGER, 'multipliers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Tm
        EXAMPLES_VALID = [consts.string.inp.TM]
        EXAMPLES_INVALID = ['hello']
