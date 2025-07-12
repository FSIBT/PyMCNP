import pymcnp
from .... import consts
from .... import classes


class Test_Fill_6:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Fill_6
        EXAMPLES_VALID = [
            {'prefix': '*', 'universe': consts.string.type.INTEGER, 'transformation': consts.string.type.INTEGER},
            {'prefix': '*', 'universe': 1, 'transformation': 1},
            {'prefix': pymcnp.types.String('*'), 'universe': consts.ast.type.INTEGER, 'transformation': consts.ast.type.INTEGER},
            {'prefix': None, 'universe': consts.string.type.INTEGER, 'transformation': consts.string.type.INTEGER},
            {'prefix': '*', 'universe': consts.string.type.INTEGER, 'transformation': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'universe': None, 'transformation': consts.string.type.INTEGER},
            {'prefix': 'hello', 'universe': consts.string.type.INTEGER, 'transformation': consts.string.type.INTEGER},
            {'prefix': '*', 'universe': consts.string.type.INTEGER, 'transformation': -9999},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Fill_6
        EXAMPLES_VALID = [consts.string.inp.like.FILL_6]
        EXAMPLES_INVALID = ['hello']
