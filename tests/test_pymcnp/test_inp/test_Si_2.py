import pymcnp
from ... import consts
from ... import classes


class Test_Si_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Si_2
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'option': 'h', 'information': [consts.string.types.DESIGNATOR]},
            {'suffix': 1, 'option': 'h', 'information': [consts.string.types.DESIGNATOR]},
            {'suffix': consts.ast.types.INTEGER, 'option': 'h', 'information': [consts.ast.types.DESIGNATOR]},
            {'suffix': consts.string.types.INTEGER, 'option': None, 'information': [consts.string.types.DESIGNATOR]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'h', 'information': [consts.string.types.DESIGNATOR]},
            {'suffix': consts.string.types.INTEGER, 'option': 'h', 'information': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Si_2
        EXAMPLES_VALID = [consts.string.inp.SI_2]
        EXAMPLES_INVALID = ['hello']
