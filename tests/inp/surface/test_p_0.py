import pymcnp
from ... import _utils


class Test_P_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.P_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.PBuilder_0
        EXAMPLES_VALID = [
            {'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL, 'c': _utils.string.type.REAL, 'd': _utils.string.type.REAL},
            {'a': 3.1, 'b': 3.1, 'c': 3.1, 'd': 3.1},
            {'a': _utils.ast.type.REAL, 'b': _utils.ast.type.REAL, 'c': _utils.ast.type.REAL, 'd': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'b': _utils.string.type.REAL, 'c': _utils.string.type.REAL, 'd': _utils.string.type.REAL},
            {'a': _utils.string.type.REAL, 'b': None, 'c': _utils.string.type.REAL, 'd': _utils.string.type.REAL},
            {'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL, 'c': None, 'd': _utils.string.type.REAL},
            {'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL, 'c': _utils.string.type.REAL, 'd': None},
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.P_0
        EXAMPLES = [
            'p 0 0 0 1',
        ]
