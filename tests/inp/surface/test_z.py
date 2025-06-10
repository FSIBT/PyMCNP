import pymcnp
from ... import _utils


class Test_Z:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.ZBuilder
        EXAMPLES_VALID = [
            {'z1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'z2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'z3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'z1': 3.1, 'r1': 3.1, 'z2': 3.1, 'r2': 3.1, 'z3': 3.1, 'r3': 3.1},
            {'z1': _utils.ast.type.REAL, 'r1': _utils.ast.type.REAL, 'z2': _utils.ast.type.REAL, 'r2': _utils.ast.type.REAL, 'z3': _utils.ast.type.REAL, 'r3': _utils.ast.type.REAL},
            {'z1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'z2': None, 'r2': _utils.string.type.REAL, 'z3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'z1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'z2': _utils.string.type.REAL, 'r2': None, 'z3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'z1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'z2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'z3': None, 'r3': _utils.string.type.REAL},
            {'z1': _utils.string.type.REAL, 'r1': _utils.string.type.REAL, 'z2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'z3': _utils.string.type.REAL, 'r3': None},
        ]
        EXAMPLES_INVALID = [
            {'z1': None, 'r1': _utils.string.type.REAL, 'z2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'z3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
            {'z1': _utils.string.type.REAL, 'r1': None, 'z2': _utils.string.type.REAL, 'r2': _utils.string.type.REAL, 'z3': _utils.string.type.REAL, 'r3': _utils.string.type.REAL},
        ]
