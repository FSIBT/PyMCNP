import pymcnp
from ... import _utils


class Test_Rec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Rec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.RecBuilder
        EXAMPLES_VALID = [
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'hx': 3.1, 'hy': 3.1, 'hz': 3.1, 'v1x': 3.1, 'v1y': 3.1, 'v1z': 3.1, 'v2x': 3.1, 'v2y': 3.1, 'v2z': 3.1},
            {
                'vx': _utils.ast.type.REAL,
                'vy': _utils.ast.type.REAL,
                'vz': _utils.ast.type.REAL,
                'hx': _utils.ast.type.REAL,
                'hy': _utils.ast.type.REAL,
                'hz': _utils.ast.type.REAL,
                'v1x': _utils.ast.type.REAL,
                'v1y': _utils.ast.type.REAL,
                'v1z': _utils.ast.type.REAL,
                'v2x': _utils.ast.type.REAL,
                'v2y': _utils.ast.type.REAL,
                'v2z': _utils.ast.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': None,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': None,
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
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': None,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': None,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': None,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': None,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': None,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': None,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': None,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': None,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
            {
                'vx': _utils.string.type.REAL,
                'vy': _utils.string.type.REAL,
                'vz': _utils.string.type.REAL,
                'hx': _utils.string.type.REAL,
                'hy': _utils.string.type.REAL,
                'hz': _utils.string.type.REAL,
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': None,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
            },
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Rec
        EXAMPLES = [
            'rec 1 2 3 4 5 6 7 8 9 1 2 3',
        ]
