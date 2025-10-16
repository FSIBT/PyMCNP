import pymcnp
from ... import consts
from ... import classes


class Test_Hsrc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Hsrc
        EXAMPLES_VALID = [
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': consts.string.types.REAL,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': consts.string.types.REAL,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': consts.string.types.REAL,
            },
            {'x_number': 1, 'x_minimum': 3.1, 'x_maximum': 3.1, 'y_number': 1, 'y_minimum': 3.1, 'y_maximum': 3.1, 'z_number': 1, 'z_minimum': 3.1, 'z_maximum': 3.1},
            {
                'x_number': consts.ast.types.INTEGER,
                'x_minimum': consts.ast.types.REAL,
                'x_maximum': consts.ast.types.REAL,
                'y_number': consts.ast.types.INTEGER,
                'y_minimum': consts.ast.types.REAL,
                'y_maximum': consts.ast.types.REAL,
                'z_number': consts.ast.types.INTEGER,
                'z_minimum': consts.ast.types.REAL,
                'z_maximum': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x_number': None,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': consts.string.types.REAL,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': consts.string.types.REAL,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': consts.string.types.REAL,
            },
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': None,
                'x_maximum': consts.string.types.REAL,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': consts.string.types.REAL,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': consts.string.types.REAL,
            },
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': None,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': consts.string.types.REAL,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': consts.string.types.REAL,
            },
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': consts.string.types.REAL,
                'y_number': None,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': consts.string.types.REAL,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': consts.string.types.REAL,
            },
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': consts.string.types.REAL,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': None,
                'y_maximum': consts.string.types.REAL,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': consts.string.types.REAL,
            },
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': consts.string.types.REAL,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': None,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': consts.string.types.REAL,
            },
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': consts.string.types.REAL,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': consts.string.types.REAL,
                'z_number': None,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': consts.string.types.REAL,
            },
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': consts.string.types.REAL,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': consts.string.types.REAL,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': None,
                'z_maximum': consts.string.types.REAL,
            },
            {
                'x_number': consts.string.types.INTEGER,
                'x_minimum': consts.string.types.REAL,
                'x_maximum': consts.string.types.REAL,
                'y_number': consts.string.types.INTEGER,
                'y_minimum': consts.string.types.REAL,
                'y_maximum': consts.string.types.REAL,
                'z_number': consts.string.types.INTEGER,
                'z_minimum': consts.string.types.REAL,
                'z_maximum': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Hsrc
        EXAMPLES_VALID = [consts.string.inp.HSRC]
        EXAMPLES_INVALID = ['hello']
