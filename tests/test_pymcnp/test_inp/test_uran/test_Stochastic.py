import pymcnp
from .... import consts
from .... import classes


class Test_Stochastic:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.uran.Stochastic
        EXAMPLES_VALID = [
            {
                'universe': consts.string.types.INTEGER,
                'maximum_x': consts.string.types.REAL,
                'maximum_y': consts.string.types.REAL,
                'maximum_z': consts.string.types.REAL,
            },
            {
                'universe': 1,
                'maximum_x': 0.5,
                'maximum_y': 0.5,
                'maximum_z': 0.5,
            },
            {
                'universe': consts.ast.types.INTEGER,
                'maximum_x': consts.ast.types.REAL,
                'maximum_y': consts.ast.types.REAL,
                'maximum_z': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'universe': None,
                'maximum_x': consts.string.types.REAL,
                'maximum_y': consts.string.types.REAL,
                'maximum_z': consts.string.types.REAL,
            },
            {
                'universe': consts.string.types.INTEGER,
                'maximum_x': None,
                'maximum_y': consts.string.types.REAL,
                'maximum_z': consts.string.types.REAL,
            },
            {
                'universe': consts.string.types.INTEGER,
                'maximum_x': consts.string.types.REAL,
                'maximum_y': None,
                'maximum_z': consts.string.types.REAL,
            },
            {
                'universe': consts.string.types.INTEGER,
                'maximum_x': consts.string.types.REAL,
                'maximum_y': consts.string.types.REAL,
                'maximum_z': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.uran.Stochastic
        EXAMPLES_VALID = [consts.string.inp.uran.STOCHASTIC]
        EXAMPLES_INVALID = ['hello']
