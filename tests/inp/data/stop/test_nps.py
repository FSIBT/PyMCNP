import pymcnp
from .... import _utils


class Test_Nps:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.stop.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.stop.NpsBuilder
        EXAMPLES_VALID = [
            {'npp': _utils.string.type.INTEGER, 'npsmg': _utils.string.type.INTEGER},
            {'npp': 1, 'npsmg': 1},
            {'npp': _utils.ast.type.INTEGER, 'npsmg': _utils.ast.type.INTEGER},
            {'npp': _utils.string.type.INTEGER, 'npsmg': None},
        ]
        EXAMPLES_INVALID = [{'npp': None, 'npsmg': _utils.string.type.INTEGER}]
