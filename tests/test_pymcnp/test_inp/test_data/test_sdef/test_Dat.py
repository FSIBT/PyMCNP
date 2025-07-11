import pymcnp
from ..... import consts
from ..... import classes


class Test_Dat:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Dat
        EXAMPLES_VALID = [
            {'month': consts.string.type.INTEGER, 'day': consts.string.type.INTEGER, 'year': consts.string.type.INTEGER},
            {'month': 1, 'day': 1, 'year': 1},
            {'month': consts.ast.type.INTEGER, 'day': consts.ast.type.INTEGER, 'year': consts.ast.type.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'month': None, 'day': consts.string.type.INTEGER, 'year': consts.string.type.INTEGER},
            {'month': consts.string.type.INTEGER, 'day': None, 'year': consts.string.type.INTEGER},
            {'month': consts.string.type.INTEGER, 'day': consts.string.type.INTEGER, 'year': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Dat
        EXAMPLES_VALID = [consts.string.inp.data.sdef.DAT]
        EXAMPLES_INVALID = ['hello']
