import pymcnp
from ..... import consts
from ..... import classes


class Test_Stochastic:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.uran.Stochastic
        EXAMPLES_VALID = [
            {
                'universe': consts.string.type.INTEGER,
                'maximum_x': consts.string.type.REAL,
                'maximum_y': consts.string.type.REAL,
                'maximum_z': consts.string.type.REAL,
            },
            {
                'universe': 1,
                'maximum_x': 0.5,
                'maximum_y': 0.5,
                'maximum_z': 0.5,
            },
            {
                'universe': consts.ast.type.INTEGER,
                'maximum_x': consts.ast.type.REAL,
                'maximum_y': consts.ast.type.REAL,
                'maximum_z': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'universe': None,
                'maximum_x': consts.string.type.REAL,
                'maximum_y': consts.string.type.REAL,
                'maximum_z': consts.string.type.REAL,
            },
            {
                'universe': consts.string.type.INTEGER,
                'maximum_x': None,
                'maximum_y': consts.string.type.REAL,
                'maximum_z': consts.string.type.REAL,
            },
            {
                'universe': consts.string.type.INTEGER,
                'maximum_x': consts.string.type.REAL,
                'maximum_y': None,
                'maximum_z': consts.string.type.REAL,
            },
            {
                'universe': consts.string.type.INTEGER,
                'maximum_x': consts.string.type.REAL,
                'maximum_y': consts.string.type.REAL,
                'maximum_z': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.uran.Stochastic
        EXAMPLES_VALID = [consts.string.inp.data.uran.STOCHASTIC]
        EXAMPLES_INVALID = ['hello']
