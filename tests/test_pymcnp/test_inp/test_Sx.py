import pymcnp
from ... import consts
from ... import classes


class Test_Sx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sx
        EXAMPLES_VALID = [
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': 1, 'transform': 1, 'x': 3.1, 'r': 3.1},
            {'prefix': pymcnp.types.String('*'), 'number': consts.ast.types.INTEGER, 'transform': consts.ast.types.INTEGER, 'x': consts.ast.types.REAL, 'r': consts.ast.types.REAL},
            {'prefix': None, 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'x': consts.string.types.REAL, 'r': consts.string.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'prefix': 'a', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': '0', 'transform': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'x': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'x': None, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sx
        EXAMPLES_VALID = [consts.string.inp.SX]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Sx
        EXAMPLES = [consts.string.inp.SX]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.SX, consts.ast.inp.SX)]
