import pymcnp
from ... import consts
from ... import classes


class Test_X:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.X
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'x1': 3.1, 'r1': 3.1, 'x2': 3.1, 'r2': 3.1, 'x3': 3.1, 'r3': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'x1': consts.ast.types.REAL,
                'r1': consts.ast.types.REAL,
                'x2': consts.ast.types.REAL,
                'r2': consts.ast.types.REAL,
                'x3': consts.ast.types.REAL,
                'r3': consts.ast.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': None,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': None,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': None,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': None,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'x1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': None,
                'r1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x1': consts.string.types.REAL,
                'r1': None,
                'x2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.X
        EXAMPLES_VALID = [
            # 3.2
            '12 X 7 5 3 2 4 3',
            consts.string.inp.X,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.X, consts.ast.inp.X)]
