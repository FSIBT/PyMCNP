import pymcnp
from .... import consts
from .... import classes


class Test_Fill_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Fill_2
        EXAMPLES_VALID = [
            {'prefix': '*', 'universe': consts.string.types.INTEGER, 'transformation': consts.string.types.TRANSFORMATION_1},
            {'prefix': '*', 'universe': 1, 'transformation': consts.string.types.TRANSFORMATION_1},
            {'prefix': pymcnp.types.String('*'), 'universe': consts.ast.types.INTEGER, 'transformation': consts.ast.types.TRANSFORMATION_1},
            {'prefix': None, 'universe': consts.string.types.INTEGER, 'transformation': consts.string.types.TRANSFORMATION_1},
            {'prefix': '*', 'universe': consts.string.types.INTEGER, 'transformation': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'universe': None, 'transformation': consts.string.types.TRANSFORMATION_1},
            {'prefix': 'hello', 'universe': consts.string.types.INTEGER, 'transformation': consts.string.types.TRANSFORMATION_1},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Fill_2
        EXAMPLES_VALID = [consts.string.inp.like.FILL_2]
        EXAMPLES_INVALID = ['hello']
