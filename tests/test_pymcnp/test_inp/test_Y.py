import pymcnp
from ... import consts
from ... import classes


class Test_Y:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Y
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'y1': 3.1, 'r1': 3.1, 'y2': 3.1, 'r2': 3.1, 'y3': 3.1, 'r3': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'y1': consts.ast.types.REAL,
                'r1': consts.ast.types.REAL,
                'y2': consts.ast.types.REAL,
                'r2': consts.ast.types.REAL,
                'y3': consts.ast.types.REAL,
                'r3': consts.ast.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': None,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': None,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': None,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': None,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'y1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': None,
                'r1': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y1': consts.string.types.REAL,
                'r1': None,
                'y2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Y
        EXAMPLES_VALID = [
            # 3.2
            '12 Y 1 2 1 3 3 4',
            '12 Y 3 0 4 1 5 0',
            '1 Y -3 2 2 1 $ surface 1',
            '2 Y 2 3 3 3 4 2 $ surface 2',
            '3 Y 2 1 4 1 4 2 $ surface 3',
            consts.string.inp.Y,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.Y, consts.ast.inp.Y)]
