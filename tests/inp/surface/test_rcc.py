import pymcnp
from ... import _utils


class Test_Rcc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.RccBuilder
        EXAMPLES_VALID = [
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'r': _utils.string.type.REAL,
            },
            {'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'hx': 3.1, 'hy': 3.1, 'hz': 3.1, 'r': 3.1},
            {
                'vx': _utils.ast.type.REAL,
                'vy': _utils.ast.type.REAL,
                'vz': _utils.ast.type.REAL,
                'hx': _utils.ast.type.REAL,
                'hy': _utils.ast.type.REAL,
                'hz': _utils.ast.type.REAL,
                'r': _utils.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': None,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'r': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': None,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'r': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': None,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'r': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': None,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'r': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': None,
                'hz': _utils.string.type.REAL,
                'r': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': None,
                'r': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'r': None,
            },
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES = ['rcc 1 2 3 4 5 6 7']
