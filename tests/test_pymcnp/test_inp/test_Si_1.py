import pymcnp
from ... import consts
from ... import classes


class Test_Si_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Si_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'option': 'h', 'information': [consts.string.types.REAL]},
            {'suffix': 1, 'option': 'h', 'information': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'option': pymcnp.types.String('h'), 'information': [consts.ast.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'option': None, 'information': [consts.string.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'h', 'information': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'option': 'h', 'information': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Si_1
        EXAMPLES_VALID = [consts.string.inp.SI_1]
        EXAMPLES_INVALID = ['hello']
