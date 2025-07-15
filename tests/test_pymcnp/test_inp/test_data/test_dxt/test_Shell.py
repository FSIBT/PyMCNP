import pymcnp
from ..... import consts
from ..... import classes


class Test_Shell:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dxt.Shell
        EXAMPLES_VALID = [
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': consts.string.type.REAL,
                'inner_radius': consts.string.type.INTEGER,
                'outer_radius': consts.string.type.INTEGER,
            },
            {
                'x': 0.5,
                'y': 0.5,
                'z': 0.5,
                'inner_radius': 1,
                'outer_radius': 1,
            },
            {
                'x': consts.ast.type.REAL,
                'y': consts.ast.type.REAL,
                'z': consts.ast.type.REAL,
                'inner_radius': consts.ast.type.INTEGER,
                'outer_radius': consts.ast.type.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.string.type.REAL,
                'z': consts.string.type.REAL,
                'inner_radius': consts.string.type.INTEGER,
                'outer_radius': consts.string.type.INTEGER,
            },
            {
                'x': consts.string.type.REAL,
                'y': None,
                'z': consts.string.type.REAL,
                'inner_radius': consts.string.type.INTEGER,
                'outer_radius': consts.string.type.INTEGER,
            },
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': None,
                'inner_radius': consts.string.type.INTEGER,
                'outer_radius': consts.string.type.INTEGER,
            },
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': consts.string.type.REAL,
                'inner_radius': None,
                'outer_radius': consts.string.type.INTEGER,
            },
            {
                'x': consts.string.type.REAL,
                'y': consts.string.type.REAL,
                'z': consts.string.type.REAL,
                'inner_radius': consts.string.type.INTEGER,
                'outer_radius': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dxt.Shell
        EXAMPLES_VALID = [consts.string.inp.data.dxt.SHELL]
        EXAMPLES_INVALID = ['hello']
