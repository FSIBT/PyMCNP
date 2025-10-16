import pymcnp
from .... import consts
from .... import classes


class Test_Dat_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Dat_0
        EXAMPLES_VALID = [
            {'month': consts.string.types.INTEGER, 'day': consts.string.types.INTEGER, 'year': consts.string.types.INTEGER},
            {'month': 1, 'day': 1, 'year': 1},
            {'month': consts.ast.types.INTEGER, 'day': consts.ast.types.INTEGER, 'year': consts.ast.types.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'month': None, 'day': consts.string.types.INTEGER, 'year': consts.string.types.INTEGER},
            {'month': consts.string.types.INTEGER, 'day': None, 'year': consts.string.types.INTEGER},
            {'month': consts.string.types.INTEGER, 'day': consts.string.types.INTEGER, 'year': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Dat_0
        EXAMPLES_VALID = [consts.string.inp.sdef.DAT_0]
        EXAMPLES_INVALID = ['hello']
