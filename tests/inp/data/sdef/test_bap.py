import pymcnp
from .... import _utils


class Test_Bap:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Bap
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.BapBuilder
        EXAMPLES_VALID = [
            {'ba1': _utils.string.type.REAL, 'ba2': _utils.string.type.REAL, 'u': _utils.string.type.REAL},
            {'ba1': 3.1, 'ba2': 3.1, 'u': 3.1},
            {'ba1': _utils.ast.type.REAL, 'ba2': _utils.ast.type.REAL, 'u': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'ba1': None, 'ba2': _utils.string.type.REAL, 'u': _utils.string.type.REAL},
            {'ba1': _utils.string.type.REAL, 'ba2': None, 'u': _utils.string.type.REAL},
            {'ba1': _utils.string.type.REAL, 'ba2': _utils.string.type.REAL, 'u': None},
        ]
