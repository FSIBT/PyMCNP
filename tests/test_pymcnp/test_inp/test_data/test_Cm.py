import pymcnp
from .... import consts
from .... import classes


class Test_Cm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Cm
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'multipliers': [consts.string.type.REAL]},
            {'suffix': 1, 'multipliers': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'multipliers': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'multipliers': [consts.string.type.REAL]}, {'suffix': consts.string.type.INTEGER, 'multipliers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Cm
        EXAMPLES_VALID = [consts.string.inp.data.CM]
        EXAMPLES_INVALID = ['hello']
