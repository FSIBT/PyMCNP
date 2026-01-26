import pymcnp
from ... import consts
from ... import classes


class Test_Pz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Pz
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
        element = pymcnp.inp.Pz
        EXAMPLES_VALID = [
            # 1.3
            '1 PZ -5',
            '1 PZ 5',
            # 3.3
            '5 pz 5',
            '6 pz -5',
            # 4.2
            '9 PZ 0.5',
            '10 PZ -0.5',
            consts.string.inp.PZ,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Pz
        EXAMPLES = [consts.string.inp.PZ]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.PZ, consts.ast.inp.PZ)]
