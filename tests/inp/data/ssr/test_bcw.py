import pymcnp
from .... import _utils


class Test_Bcw:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Bcw
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.BcwBuilder
        EXAMPLES_VALID = [
            {'radius': _utils.string.type.REAL, 'zb': '0.8', 'ze': _utils.string.type.REAL},
            {'radius': 3.1, 'zb': 0.8, 'ze': 3.1},
            {'radius': _utils.ast.type.REAL, 'zb': pymcnp.utils.types.Real(0.8), 'ze': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'radius': None, 'zb': '0.8', 'ze': _utils.string.type.REAL},
            {'radius': _utils.string.type.REAL, 'zb': None, 'ze': _utils.string.type.REAL},
            {'radius': _utils.string.type.REAL, 'zb': '0.8', 'ze': None},
            {'radius': _utils.string.type.REAL, 'zb': '3.1', 'ze': _utils.string.type.REAL},
        ]
