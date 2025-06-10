import pymcnp
from ... import _utils


class Test_Rpp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.RppBuilder
        EXAMPLES_VALID = [
            {
                'xmin': _utils.string.type.REAL,
                'xmax': _utils.string.type.REAL,
                'ymin': _utils.string.type.REAL,
                'ymax': _utils.string.type.REAL,
                'zmin': _utils.string.type.REAL,
                'zmax': _utils.string.type.REAL,
            },
            {'xmin': 3.1, 'xmax': 3.1, 'ymin': 3.1, 'ymax': 3.1, 'zmin': 3.1, 'zmax': 3.1},
            {
                'xmin': _utils.ast.type.REAL,
                'xmax': _utils.ast.type.REAL,
                'ymin': _utils.ast.type.REAL,
                'ymax': _utils.ast.type.REAL,
                'zmin': _utils.ast.type.REAL,
                'zmax': _utils.ast.type.REAL,
            },
            {'xmin': _utils.string.type.REAL, 'xmax': _utils.string.type.REAL, 'ymin': _utils.string.type.REAL, 'ymax': _utils.string.type.REAL, 'zmin': None, 'zmax': _utils.string.type.REAL},
            {'xmin': _utils.string.type.REAL, 'xmax': _utils.string.type.REAL, 'ymin': _utils.string.type.REAL, 'ymax': _utils.string.type.REAL, 'zmin': _utils.string.type.REAL, 'zmax': None},
        ]
        EXAMPLES_INVALID = [
            {'xmin': None, 'xmax': _utils.string.type.REAL, 'ymin': _utils.string.type.REAL, 'ymax': _utils.string.type.REAL, 'zmin': _utils.string.type.REAL, 'zmax': _utils.string.type.REAL},
            {'xmin': _utils.string.type.REAL, 'xmax': None, 'ymin': _utils.string.type.REAL, 'ymax': _utils.string.type.REAL, 'zmin': _utils.string.type.REAL, 'zmax': _utils.string.type.REAL},
            {'xmin': _utils.string.type.REAL, 'xmax': _utils.string.type.REAL, 'ymin': None, 'ymax': _utils.string.type.REAL, 'zmin': _utils.string.type.REAL, 'zmax': _utils.string.type.REAL},
            {'xmin': _utils.string.type.REAL, 'xmax': _utils.string.type.REAL, 'ymin': _utils.string.type.REAL, 'ymax': None, 'zmin': _utils.string.type.REAL, 'zmax': _utils.string.type.REAL},
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES = ['rpp 1 2 3 4 5 6']
