import pymcnp
from ... import consts
from ... import classes


class Test_K_x:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.K_x
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'x': 3.1, 'y': 3.1, 'z': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                't_squared': consts.ast.types.REAL,
                'plusminus_1': consts.ast.types.REAL,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': None,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': None,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': None,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': None,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.K_x
        EXAMPLES_VALID = [consts.string.inp.K_X]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.K_x
        EXAMPLES = [consts.string.inp.K_X]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.K_X, consts.ast.inp.K_X)]
