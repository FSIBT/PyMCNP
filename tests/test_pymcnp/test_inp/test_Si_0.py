import pymcnp
from ... import consts
from ... import classes


class Test_Si_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Si_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'option': 'h', 'information': [consts.string.types.DISTRIBUTION]},
            {'suffix': 1, 'option': 'h', 'information': [consts.string.types.DISTRIBUTION]},
            {'suffix': consts.ast.types.INTEGER, 'option': pymcnp.types.String('h'), 'information': [consts.ast.types.DISTRIBUTION]},
            {'suffix': consts.string.types.INTEGER, 'option': None, 'information': [consts.string.types.DISTRIBUTION]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'h', 'information': [consts.string.types.DISTRIBUTION]},
            {'suffix': consts.string.types.INTEGER, 'option': 'h', 'information': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Si_0
        EXAMPLES_VALID = [consts.string.inp.SI_0]
        EXAMPLES_INVALID = ['hello']
