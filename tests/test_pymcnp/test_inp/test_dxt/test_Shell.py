import pymcnp
from .... import consts
from .... import classes


class Test_Shell:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dxt.Shell
        EXAMPLES_VALID = [
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'inner_radius': consts.string.types.INTEGER,
                'outer_radius': consts.string.types.INTEGER,
            },
            {
                'x': 0.5,
                'y': 0.5,
                'z': 0.5,
                'inner_radius': 1,
                'outer_radius': 1,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'inner_radius': consts.ast.types.INTEGER,
                'outer_radius': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'inner_radius': consts.string.types.INTEGER,
                'outer_radius': consts.string.types.INTEGER,
            },
            {
                'x': consts.string.types.REAL,
                'y': None,
                'z': consts.string.types.REAL,
                'inner_radius': consts.string.types.INTEGER,
                'outer_radius': consts.string.types.INTEGER,
            },
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': None,
                'inner_radius': consts.string.types.INTEGER,
                'outer_radius': consts.string.types.INTEGER,
            },
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'inner_radius': None,
                'outer_radius': consts.string.types.INTEGER,
            },
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'inner_radius': consts.string.types.INTEGER,
                'outer_radius': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dxt.Shell
        EXAMPLES_VALID = [consts.string.inp.dxt.SHELL]
        EXAMPLES_INVALID = ['hello']
