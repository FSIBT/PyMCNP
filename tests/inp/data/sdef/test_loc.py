import pymcnp
from .... import _utils


class Test_Loc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Loc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.LocBuilder
        EXAMPLES_VALID = [
            {'latitude': _utils.string.type.REAL, 'longitude': _utils.string.type.REAL, 'altitude': _utils.string.type.REAL},
            {'latitude': 3.1, 'longitude': 3.1, 'altitude': 3.1},
            {'latitude': _utils.ast.type.REAL, 'longitude': _utils.ast.type.REAL, 'altitude': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'latitude': None, 'longitude': _utils.string.type.REAL, 'altitude': _utils.string.type.REAL},
            {'latitude': _utils.string.type.REAL, 'longitude': None, 'altitude': _utils.string.type.REAL},
            {'latitude': _utils.string.type.REAL, 'longitude': _utils.string.type.REAL, 'altitude': None},
        ]
