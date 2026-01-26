import pymcnp
from ... import consts
from ... import classes


class Test_Sy:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sy
        EXAMPLES_VALID = [
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': 1, 'transform': 1, 'y': 3.1, 'r': 3.1},
            {'prefix': pymcnp.types.String('*'), 'number': consts.ast.types.INTEGER, 'transform': consts.ast.types.INTEGER, 'y': consts.ast.types.REAL, 'r': consts.ast.types.REAL},
            {'prefix': None, 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'prefix': 'a', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': '0', 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'y': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': None, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sy
        EXAMPLES_VALID = [consts.string.inp.SY]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Sy
        EXAMPLES = [consts.string.inp.SY]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.SY, consts.ast.inp.SY)]
