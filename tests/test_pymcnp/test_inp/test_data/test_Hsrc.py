import pymcnp
from .... import consts
from .... import classes


class Test_Hsrc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Hsrc
        EXAMPLES_VALID = [
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': consts.string.type.REAL,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': consts.string.type.REAL,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': consts.string.type.REAL,
            },
            {'x_number': 1, 'x_minimum': 3.1, 'x_maximum': 3.1, 'y_number': 1, 'y_minimum': 3.1, 'y_maximum': 3.1, 'z_number': 1, 'z_minimum': 3.1, 'z_maximum': 3.1},
            {
                'x_number': consts.ast.type.INTEGER,
                'x_minimum': consts.ast.type.REAL,
                'x_maximum': consts.ast.type.REAL,
                'y_number': consts.ast.type.INTEGER,
                'y_minimum': consts.ast.type.REAL,
                'y_maximum': consts.ast.type.REAL,
                'z_number': consts.ast.type.INTEGER,
                'z_minimum': consts.ast.type.REAL,
                'z_maximum': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x_number': None,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': consts.string.type.REAL,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': consts.string.type.REAL,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': consts.string.type.REAL,
            },
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': None,
                'x_maximum': consts.string.type.REAL,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': consts.string.type.REAL,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': consts.string.type.REAL,
            },
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': None,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': consts.string.type.REAL,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': consts.string.type.REAL,
            },
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': consts.string.type.REAL,
                'y_number': None,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': consts.string.type.REAL,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': consts.string.type.REAL,
            },
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': consts.string.type.REAL,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': None,
                'y_maximum': consts.string.type.REAL,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': consts.string.type.REAL,
            },
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': consts.string.type.REAL,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': None,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': consts.string.type.REAL,
            },
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': consts.string.type.REAL,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': consts.string.type.REAL,
                'z_number': None,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': consts.string.type.REAL,
            },
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': consts.string.type.REAL,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': consts.string.type.REAL,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': None,
                'z_maximum': consts.string.type.REAL,
            },
            {
                'x_number': consts.string.type.INTEGER,
                'x_minimum': consts.string.type.REAL,
                'x_maximum': consts.string.type.REAL,
                'y_number': consts.string.type.INTEGER,
                'y_minimum': consts.string.type.REAL,
                'y_maximum': consts.string.type.REAL,
                'z_number': consts.string.type.INTEGER,
                'z_minimum': consts.string.type.REAL,
                'z_maximum': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Hsrc
        EXAMPLES_VALID = [consts.string.inp.data.HSRC]
        EXAMPLES_INVALID = ['hello']
