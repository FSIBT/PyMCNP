import pymcnp
from ... import consts
from ... import classes


class Test_Tr_4:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Tr_4
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'system': consts.string.types.INTEGER},
            {'prefix': '*', 'suffix': 1, 'x': 3.1, 'y': 3.1, 'z': 3.1, 'system': 1},
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': consts.ast.types.INTEGER,
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'system': consts.ast.types.INTEGER,
            },
            {'prefix': None, 'suffix': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'system': consts.string.types.INTEGER},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'system': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'system': consts.string.types.INTEGER},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'x': None, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'system': consts.string.types.INTEGER},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'y': None, 'z': consts.string.types.REAL, 'system': consts.string.types.INTEGER},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': None, 'system': consts.string.types.INTEGER},
            {
                'prefix': 'hello',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL, 'system': -9999},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Tr_4
        EXAMPLES_VALID = [consts.string.inp.TR_4]
        EXAMPLES_INVALID = ['hello']
