import pymcnp
from ... import consts
from ... import classes


class Test_Ky:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ky
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'y': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'y': consts.ast.types.REAL,
                't_squared': consts.ast.types.REAL,
                'plusminus_1': consts.ast.types.REAL,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'y': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'y': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'y': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'y': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': None, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 't_squared': None, 'plusminus_1': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'y': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ky
        EXAMPLES_VALID = [consts.string.inp.KY]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Ky
        EXAMPLES = [consts.string.inp.KY]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.KY, consts.ast.inp.KY)]
