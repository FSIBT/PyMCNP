import pymcnp
from ... import _utils


class Test_Wwg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.WwgBuilder
        EXAMPLES_VALID = [
            {'tally': _utils.string.type.INTEGER, 'cell': _utils.string.type.INTEGER, 'lower': _utils.string.type.REAL, 'setting': _utils.string.type.INTEGER},
            {'tally': 1, 'cell': 1, 'lower': 3.1, 'setting': 1},
            {'tally': _utils.ast.type.INTEGER, 'cell': _utils.ast.type.INTEGER, 'lower': _utils.ast.type.REAL, 'setting': _utils.ast.type.INTEGER},
            {'tally': _utils.string.type.INTEGER, 'cell': _utils.string.type.INTEGER, 'lower': _utils.string.type.REAL, 'setting': None},
        ]
        EXAMPLES_INVALID = [
            {'tally': None, 'cell': _utils.string.type.INTEGER, 'lower': _utils.string.type.REAL, 'setting': _utils.string.type.INTEGER},
            {'tally': _utils.string.type.INTEGER, 'cell': None, 'lower': _utils.string.type.REAL, 'setting': _utils.string.type.INTEGER},
            {'tally': _utils.string.type.INTEGER, 'cell': _utils.string.type.INTEGER, 'lower': None, 'setting': _utils.string.type.INTEGER},
        ]
