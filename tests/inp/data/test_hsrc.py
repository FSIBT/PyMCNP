import pymcnp
from ... import _utils


class Test_Hsrc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Hsrc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.HsrcBuilder
        EXAMPLES_VALID = [
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': _utils.string.type.REAL,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': _utils.string.type.REAL,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': _utils.string.type.REAL,
            },
            {'x_number': 1, 'x_minimum': 3.1, 'x_maximum': 3.1, 'y_number': 1, 'y_minimum': 3.1, 'y_maximum': 3.1, 'z_number': 1, 'z_minimum': 3.1, 'z_maximum': 3.1},
            {
                'x_number': _utils.ast.type.INTEGER,
                'x_minimum': _utils.ast.type.REAL,
                'x_maximum': _utils.ast.type.REAL,
                'y_number': _utils.ast.type.INTEGER,
                'y_minimum': _utils.ast.type.REAL,
                'y_maximum': _utils.ast.type.REAL,
                'z_number': _utils.ast.type.INTEGER,
                'z_minimum': _utils.ast.type.REAL,
                'z_maximum': _utils.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x_number': None,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': _utils.string.type.REAL,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': _utils.string.type.REAL,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': _utils.string.type.REAL,
            },
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': None,
                'x_maximum': _utils.string.type.REAL,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': _utils.string.type.REAL,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': _utils.string.type.REAL,
            },
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': None,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': _utils.string.type.REAL,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': _utils.string.type.REAL,
            },
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': _utils.string.type.REAL,
                'y_number': None,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': _utils.string.type.REAL,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': _utils.string.type.REAL,
            },
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': _utils.string.type.REAL,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': None,
                'y_maximum': _utils.string.type.REAL,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': _utils.string.type.REAL,
            },
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': _utils.string.type.REAL,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': None,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': _utils.string.type.REAL,
            },
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': _utils.string.type.REAL,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': _utils.string.type.REAL,
                'z_number': None,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': _utils.string.type.REAL,
            },
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': _utils.string.type.REAL,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': _utils.string.type.REAL,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': None,
                'z_maximum': _utils.string.type.REAL,
            },
            {
                'x_number': _utils.string.type.INTEGER,
                'x_minimum': _utils.string.type.REAL,
                'x_maximum': _utils.string.type.REAL,
                'y_number': _utils.string.type.INTEGER,
                'y_minimum': _utils.string.type.REAL,
                'y_maximum': _utils.string.type.REAL,
                'z_number': _utils.string.type.INTEGER,
                'z_minimum': _utils.string.type.REAL,
                'z_maximum': None,
            },
        ]
