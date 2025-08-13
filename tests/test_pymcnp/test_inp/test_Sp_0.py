import pymcnp
from ... import consts
from ... import classes


class Test_Sp_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sp_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'option': 'd', 'probabilities': [consts.string.types.REAL]},
            {'suffix': 1, 'option': 'd', 'probabilities': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'option': pymcnp.types.String('d'), 'probabilities': [consts.ast.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'option': None, 'probabilities': [consts.string.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'd', 'probabilities': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'option': 'd', 'probabilities': None},
            {'suffix': consts.string.types.INTEGER, 'option': 'hello', 'probabilities': [consts.string.types.REAL]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sp_0
        EXAMPLES_VALID = [consts.string.inp.SP_0]
        EXAMPLES_INVALID = ['hello']
