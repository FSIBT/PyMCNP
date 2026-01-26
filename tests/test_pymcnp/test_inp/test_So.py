import pymcnp
from ... import consts
from ... import classes


class Test_So:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.So
        EXAMPLES_VALID = [
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': 1, 'transform': 1, 'r': 3.1},
            {'prefix': pymcnp.types.String('*'), 'number': consts.ast.types.INTEGER, 'transform': consts.ast.types.INTEGER, 'r': consts.ast.types.REAL},
            {'prefix': None, 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'r': consts.string.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'prefix': 'a', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': '0', 'transform': consts.string.types.INTEGER, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.So
        EXAMPLES_VALID = [
            # 4.1
            '8 SO 8',
            consts.string.inp.SO,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.So
        EXAMPLES = [consts.string.inp.SO]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.SO, consts.ast.inp.SO)]
