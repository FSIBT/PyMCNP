import pymcnp
from ... import _utils


class Test_Tx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Tx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.TxBuilder
        EXAMPLES_VALID = [
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL, 'c': _utils.string.type.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1, 'a': 3.1, 'b': 3.1, 'c': 3.1},
            {'x': _utils.ast.type.REAL, 'y': _utils.ast.type.REAL, 'z': _utils.ast.type.REAL, 'a': _utils.ast.type.REAL, 'b': _utils.ast.type.REAL, 'c': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL, 'c': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': None, 'z': _utils.string.type.REAL, 'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL, 'c': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': None, 'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL, 'c': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 'a': None, 'b': _utils.string.type.REAL, 'c': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 'a': _utils.string.type.REAL, 'b': None, 'c': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL, 'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL, 'c': None},
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Tx
        EXAMPLES = ['tx 1 2 3 4 5 6']
