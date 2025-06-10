import pymcnp
from .... import _utils


class Test_Axs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.AxsBuilder
        EXAMPLES_VALID = [
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1},
            {'x': _utils.ast.type.REAL, 'y': _utils.ast.type.REAL, 'z': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': _utils.string.type.REAL, 'z': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': None, 'z': _utils.string.type.REAL},
            {'x': _utils.string.type.REAL, 'y': _utils.string.type.REAL, 'z': None},
        ]
