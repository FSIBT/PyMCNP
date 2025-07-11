import pymcnp
from .... import consts
from .... import classes


class Test_Si_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Si_2
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'option': consts.string.type.STRING, 'information': [consts.string.type.DESIGNATOR]},
            {'suffix': 1, 'option': consts.string.type.STRING, 'information': [consts.string.type.DESIGNATOR]},
            {'suffix': consts.ast.type.INTEGER, 'option': consts.ast.type.STRING, 'information': [consts.ast.type.DESIGNATOR]},
            {'suffix': consts.string.type.INTEGER, 'option': None, 'information': [consts.string.type.DESIGNATOR]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': consts.string.type.STRING, 'information': [consts.string.type.DESIGNATOR]},
            {'suffix': consts.string.type.INTEGER, 'option': consts.string.type.STRING, 'information': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Si_2
        EXAMPLES_VALID = [consts.string.inp.data.SI_2]
        EXAMPLES_INVALID = ['hello']
