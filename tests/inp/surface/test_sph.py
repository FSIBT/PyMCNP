import pymcnp
from ... import _utils


class Test_Sph:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sph
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SphBuilder
        EXAMPLES_VALID = [
            {'vx': _utils.string.type.REAL, 'vy': _utils.string.type.REAL, 'vz': _utils.string.type.REAL, 'r': _utils.string.type.REAL},
            {'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'r': 3.1},
            {'vx': _utils.ast.type.REAL, 'vy': _utils.ast.type.REAL, 'vz': _utils.ast.type.REAL, 'r': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'vx': None, 'vy': _utils.string.type.REAL, 'vz': _utils.string.type.REAL, 'r': _utils.string.type.REAL},
            {'vx': _utils.string.type.REAL, 'vy': None, 'vz': _utils.string.type.REAL, 'r': _utils.string.type.REAL},
            {'vx': _utils.string.type.REAL, 'vy': _utils.string.type.REAL, 'vz': None, 'r': _utils.string.type.REAL},
            {'vx': _utils.string.type.REAL, 'vy': _utils.string.type.REAL, 'vz': _utils.string.type.REAL, 'r': None},
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Sph
        EXAMPLES = ['sph 1 2 3 4']
