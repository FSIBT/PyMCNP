import pymcnp
from .... import consts
from .... import classes


class Test_Si_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Si_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'option': consts.string.type.STRING, 'information': [consts.string.type.REAL]},
            {'suffix': 1, 'option': consts.string.type.STRING, 'information': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'option': consts.ast.type.STRING, 'information': [consts.ast.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'option': None, 'information': [consts.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': consts.string.type.STRING, 'information': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'option': consts.string.type.STRING, 'information': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Si_1
        EXAMPLES_VALID = [consts.string.inp.data.SI_1]
        EXAMPLES_INVALID = ['hello']
