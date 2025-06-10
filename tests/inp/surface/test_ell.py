import pymcnp
from ... import _utils


class Test_Ell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Ell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.EllBuilder
        EXAMPLES_VALID = [
            {
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
                'rm': _utils.string.type.REAL,
            },
            {'v1x': 3.1, 'v1y': 3.1, 'v1z': 3.1, 'v2x': 3.1, 'v2y': 3.1, 'v2z': 3.1, 'rm': 3.1},
            {
                'v1x': _utils.ast.type.REAL,
                'v1y': _utils.ast.type.REAL,
                'v1z': _utils.ast.type.REAL,
                'v2x': _utils.ast.type.REAL,
                'v2y': _utils.ast.type.REAL,
                'v2z': _utils.ast.type.REAL,
                'rm': _utils.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'v1x': None,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
                'rm': _utils.string.type.REAL,
            },
            {
                'v1x': _utils.string.type.REAL,
                'v1y': None,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
                'rm': _utils.string.type.REAL,
            },
            {
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': None,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
                'rm': _utils.string.type.REAL,
            },
            {
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': None,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
                'rm': _utils.string.type.REAL,
            },
            {
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': None,
                'v2z': _utils.string.type.REAL,
                'rm': _utils.string.type.REAL,
            },
            {
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': None,
                'rm': _utils.string.type.REAL,
            },
            {
                'v1x': _utils.string.type.REAL,
                'v1y': _utils.string.type.REAL,
                'v1z': _utils.string.type.REAL,
                'v2x': _utils.string.type.REAL,
                'v2y': _utils.string.type.REAL,
                'v2z': _utils.string.type.REAL,
                'rm': None,
            },
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Ell
        EXAMPLES = [
            'ell 1 2 3 4 5 6 7',
            'ell 1 2 3 4 5 6 -7',
        ]
