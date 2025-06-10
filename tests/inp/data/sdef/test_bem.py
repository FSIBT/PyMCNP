import pymcnp
from .... import _utils


class Test_Bem:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Bem
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.BemBuilder
        EXAMPLES_VALID = [
            {'exn': _utils.string.type.REAL, 'eyn': _utils.string.type.REAL, 'bml': _utils.string.type.REAL},
            {'exn': 3.1, 'eyn': 3.1, 'bml': 3.1},
            {'exn': _utils.ast.type.REAL, 'eyn': _utils.ast.type.REAL, 'bml': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'exn': None, 'eyn': _utils.string.type.REAL, 'bml': _utils.string.type.REAL},
            {'exn': _utils.string.type.REAL, 'eyn': None, 'bml': _utils.string.type.REAL},
            {'exn': _utils.string.type.REAL, 'eyn': _utils.string.type.REAL, 'bml': None},
        ]
