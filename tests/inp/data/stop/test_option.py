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
            {'npp': '1', 'npsmg': '1'},
            {'npp': '1', 'npsmg': None},
            {'npp': 1, 'npsmg': 1},
            {'npp': _utils.INTEGER, 'npsmg': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [{'npp': None, 'npsmg': '1'}]


class Test_Ctme:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.stop.Ctme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.stop.CtmeBuilder
        EXAMPLES_VALID = [{'tme': '1.0'}, {'tme': 1.0}, {'tme': _utils.REAL}]
        EXAMPLES_INVALID = [{'tme': None}]


class Test_Fk:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.stop.Fk
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.stop.FkBuilder
        EXAMPLES_VALID = [
            {'e': '1', 'suffix': '1'},
            {'e': 1, 'suffix': 1},
            {'e': _utils.INTEGER, 'suffix': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [{'e': None, 'suffix': '1'}, {'e': '1', 'suffix': None}]
