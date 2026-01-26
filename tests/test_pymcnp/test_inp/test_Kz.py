import pymcnp
from ... import consts
from ... import classes


class Test_Kz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Kz
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'z': 3.1, 't_squared': 3.1, 'plusminus_1': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'z': consts.ast.types.REAL,
                't_squared': consts.ast.types.REAL,
                'plusminus_1': consts.ast.types.REAL,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'z': consts.string.types.REAL,
                't_squared': consts.string.types.REAL,
                'plusminus_1': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'z': None, 't_squared': consts.string.types.REAL, 'plusminus_1': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 't_squared': None, 'plusminus_1': consts.string.types.REAL},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'z': consts.string.types.REAL, 't_squared': consts.string.types.REAL, 'plusminus_1': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Kz
        EXAMPLES_VALID = [
            # 4.1
            '5 kz 8 0.25 -1',
            consts.string.inp.KZ,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Kz
        EXAMPLES = [consts.string.inp.KZ]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.KZ, consts.ast.inp.KZ)]
