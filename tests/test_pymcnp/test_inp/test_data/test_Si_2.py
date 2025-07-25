import pymcnp
from .... import consts
from .... import classes


class Test_Si_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Si_2
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'option': consts.string.types.STRING, 'information': [consts.string.types.DESIGNATOR]},
            {'suffix': 1, 'option': consts.string.types.STRING, 'information': [consts.string.types.DESIGNATOR]},
            {'suffix': consts.ast.types.INTEGER, 'option': consts.ast.types.STRING, 'information': [consts.ast.types.DESIGNATOR]},
            {'suffix': consts.string.types.INTEGER, 'option': None, 'information': [consts.string.types.DESIGNATOR]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': consts.string.types.STRING, 'information': [consts.string.types.DESIGNATOR]},
            {'suffix': consts.string.types.INTEGER, 'option': consts.string.types.STRING, 'information': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Si_2
        EXAMPLES_VALID = [consts.string.inp.data.SI_2]
        EXAMPLES_INVALID = ['hello']
