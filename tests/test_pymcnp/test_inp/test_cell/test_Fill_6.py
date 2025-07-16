import pymcnp
from .... import consts
from .... import classes


class Test_Fill_6:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Fill_6
        EXAMPLES_VALID = [
            {'prefix': '*', 'universe': consts.string.types.INTEGER, 'transformation': consts.string.types.INTEGER},
            {'prefix': '*', 'universe': 1, 'transformation': 1},
            {'prefix': pymcnp.types.String('*'), 'universe': consts.ast.types.INTEGER, 'transformation': consts.ast.types.INTEGER},
            {'prefix': None, 'universe': consts.string.types.INTEGER, 'transformation': consts.string.types.INTEGER},
            {'prefix': '*', 'universe': consts.string.types.INTEGER, 'transformation': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'universe': None, 'transformation': consts.string.types.INTEGER},
            {'prefix': 'hello', 'universe': consts.string.types.INTEGER, 'transformation': consts.string.types.INTEGER},
            {'prefix': '*', 'universe': consts.string.types.INTEGER, 'transformation': -9999},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Fill_6
        EXAMPLES_VALID = [consts.string.inp.cell.FILL_6]
        EXAMPLES_INVALID = ['hello']
