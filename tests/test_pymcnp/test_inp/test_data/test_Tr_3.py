import pymcnp
from .... import consts
from .... import classes


class Test_Tr_3:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Tr_3
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {'prefix': '*', 'suffix': 1, 'x': 3.1, 'y': 3.1, 'z': 3.1, 'xx': 3.1, 'xy': 3.1, 'xz': 3.1, 'system': 1},
            {
                'prefix': pymcnp.types.String('*'),
                'suffix': consts.ast.types.INTEGER,
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'xx': consts.ast.types.REAL,
                'xy': consts.ast.types.REAL,
                'xz': consts.ast.types.REAL,
                'system': consts.ast.types.INTEGER,
            },
            {
                'prefix': None,
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': '*',
                'suffix': None,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': None,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': None,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': None,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': None,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': None,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': None,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': 'hello',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': consts.string.types.INTEGER,
            },
            {
                'prefix': '*',
                'suffix': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'xx': consts.string.types.REAL,
                'xy': consts.string.types.REAL,
                'xz': consts.string.types.REAL,
                'system': -9999,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Tr_3
        EXAMPLES_VALID = [consts.string.inp.data.TR_3]
        EXAMPLES_INVALID = ['hello']
