import pymcnp
from ... import consts
from ... import classes


class Test_Sb_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sb_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'option': 'd', 'biases': [consts.string.types.REAL]},
            {'suffix': 1, 'option': 'd', 'biases': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'option': pymcnp.types.String('d'), 'biases': [consts.ast.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'option': None, 'biases': [consts.string.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'd', 'biases': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'option': 'd', 'biases': None},
            {'suffix': consts.string.types.INTEGER, 'option': 'hello', 'biases': [consts.string.types.REAL]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sb_0
        EXAMPLES_VALID = [consts.string.inp.SB_0]
        EXAMPLES_INVALID = ['hello']
