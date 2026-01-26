import pymcnp
from ... import consts
from ... import classes


class Test_Sph:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sph
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'r': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'vx': consts.ast.types.REAL,
                'vy': consts.ast.types.REAL,
                'vz': consts.ast.types.REAL,
                'r': consts.ast.types.REAL,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': None,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': None,
                'vz': consts.string.types.REAL,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': None,
                'r': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'r': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sph
        EXAMPLES_VALID = [consts.string.inp.SPH]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Sph
        EXAMPLES = [consts.string.inp.SPH]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.SPH, consts.ast.inp.SPH)]
