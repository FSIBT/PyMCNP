import pymcnp
from ... import consts
from ... import classes


class Test_Sz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sz
        EXAMPLES_VALID = [
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': 1, 'transform': 1, 'z': 3.1, 'r': 3.1},
            {'prefix': pymcnp.types.String('*'), 'number': consts.ast.types.INTEGER, 'transform': consts.ast.types.INTEGER, 'z': consts.ast.types.REAL, 'r': consts.ast.types.REAL},
            {'prefix': None, 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'prefix': 'a', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': '0', 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'z': None, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sz
        EXAMPLES_VALID = [consts.string.inp.SZ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Sz
        EXAMPLES = [consts.string.inp.SZ]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.SZ, consts.ast.inp.SZ)]
