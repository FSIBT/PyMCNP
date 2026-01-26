import pymcnp
from ... import consts
from ... import classes


class Test_C_x:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.C_x
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'y': 3.1, 'z': 3.1, 'r': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'r': consts.ast.types.REAL,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': None, 'z': consts.string.types.REAL, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'z': None, 'r': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'r': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.C_x
        EXAMPLES_VALID = [consts.string.inp.C_X]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.C_x
        EXAMPLES = [consts.string.inp.C_X]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.C_X, consts.ast.inp.C_X)]
