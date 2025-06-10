import pymcnp
from ... import _utils


class Test_Prdmp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Prdmp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.PrdmpBuilder
        EXAMPLES_VALID = [
            {'ndp': _utils.string.type.INTEGER, 'ndm': _utils.string.type.INTEGER, 'mct': _utils.string.type.INTEGER, 'ndmp': _utils.string.type.INTEGER, 'dmmp': _utils.string.type.INTEGER},
            {'ndp': 1, 'ndm': 1, 'mct': 1, 'ndmp': 1, 'dmmp': 1},
            {'ndp': _utils.ast.type.INTEGER, 'ndm': _utils.ast.type.INTEGER, 'mct': _utils.ast.type.INTEGER, 'ndmp': _utils.ast.type.INTEGER, 'dmmp': _utils.ast.type.INTEGER},
            {'ndp': None, 'ndm': _utils.string.type.INTEGER, 'mct': _utils.string.type.INTEGER, 'ndmp': _utils.string.type.INTEGER, 'dmmp': _utils.string.type.INTEGER},
            {'ndp': _utils.string.type.INTEGER, 'ndm': None, 'mct': _utils.string.type.INTEGER, 'ndmp': _utils.string.type.INTEGER, 'dmmp': _utils.string.type.INTEGER},
            {'ndp': _utils.string.type.INTEGER, 'ndm': _utils.string.type.INTEGER, 'mct': None, 'ndmp': _utils.string.type.INTEGER, 'dmmp': _utils.string.type.INTEGER},
            {'ndp': _utils.string.type.INTEGER, 'ndm': _utils.string.type.INTEGER, 'mct': _utils.string.type.INTEGER, 'ndmp': None, 'dmmp': _utils.string.type.INTEGER},
            {'ndp': _utils.string.type.INTEGER, 'ndm': _utils.string.type.INTEGER, 'mct': _utils.string.type.INTEGER, 'ndmp': _utils.string.type.INTEGER, 'dmmp': None},
        ]
        EXAMPLES_INVALID = []
