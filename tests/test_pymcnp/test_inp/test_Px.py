import pymcnp
from ... import consts
from ... import classes


class Test_Px:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Px
        EXAMPLES_VALID = [
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'd': consts.string.types.REAL},
            {'prefix': '*', 'number': 1, 'transform': 1, 'd': 3.1},
            {'prefix': pymcnp.types.String('*'), 'number': consts.ast.types.INTEGER, 'transform': consts.ast.types.INTEGER, 'd': consts.ast.types.REAL},
            {'prefix': None, 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'd': consts.string.types.REAL},
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'd': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'd': consts.string.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'prefix': 'a', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'd': consts.string.types.REAL},
            {'prefix': '*', 'number': '0', 'transform': consts.string.types.INTEGER, 'd': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'd': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'd': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Px
        EXAMPLES_VALID = [consts.string.inp.PX]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Px
        EXAMPLES = [
            # 1.3
            '1 PX 5',
            '1 PX -5',
            # 3.3
            '11 4 PX 5',
            '1 px 0',
            '2 px 50',
            '7 px 10',
            # 4.1
            '1 PX 0 $ plane perpendicular to the X axis at x=0',
            '3 PX 2 $ plane perpendicular to the X axis at x=2',
            '5 PX 6 $ plane perpendicular to the X axis at x=6',
            '1 PX -3',
            '3 PX -1',
            '5 PX 1',
            '7 PX 3',
            # 4.2
            '7 PX 0.5',
            '8 PX -0.5',
            consts.string.inp.PX,
        ]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.PX, consts.ast.inp.PX)]
