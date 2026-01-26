import pymcnp
from ... import consts
from ... import classes


class Test_Cx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Cx
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
        element = pymcnp.inp.Cx
        EXAMPLES_VALID = [
            # 3.2
            '11 7 CX 1',
            # 4.1
            '2 CX 2 $ cylinder on the X axis of radius 2',
            '4 CX 3 $ cylinder on the X axis of radius 3',
            '2 CX 2',
            '4 CX 5',
            '6 CX 3.5',
            consts.string.inp.CX,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Cx
        EXAMPLES = [consts.string.inp.CX]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.CX, consts.ast.inp.CX)]
