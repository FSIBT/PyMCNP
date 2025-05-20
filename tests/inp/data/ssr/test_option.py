import pymcnp
from .... import _utils


class Test_Old:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Old
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.OldBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Cel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.CelBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_New:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.New
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.NewBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Pty:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Pty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.PtyBuilder
        EXAMPLES_VALID = [{'particles': ['n']}, {'particles': [_utils.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]


class Test_Col:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Col
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.ColBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Wgt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Wgt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.WgtBuilder
        EXAMPLES_VALID = [{'constant': '1.0'}, {'constant': 1.0}, {'constant': _utils.REAL}]
        EXAMPLES_INVALID = [{'constant': None}]


class Test_Tr_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Tr_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.TrBuilder_0
        EXAMPLES_VALID = [{'number': 'd1'}, {'number': _utils.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Tr_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Tr_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.TrBuilder_1
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Psc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Psc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.PscBuilder
        EXAMPLES_VALID = [{'constant': '1.0'}, {'constant': 1.0}, {'constant': _utils.REAL}]
        EXAMPLES_INVALID = [{'constant': None}]


class Test_Axs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.AxsBuilder
        EXAMPLES_VALID = [{'cosines': ['1.0']}, {'cosines': [1.0]}, {'cosines': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'cosines': None}]


class Test_Ext:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.ExtBuilder
        EXAMPLES_VALID = [{'number': 'd1'}, {'number': _utils.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Poa:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Poa
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.PoaBuilder
        EXAMPLES_VALID = [{'angle': '1.0'}, {'angle': 1.0}, {'angle': _utils.REAL}]
        EXAMPLES_INVALID = [{'angle': None}]


class Test_Bcw:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Bcw
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.BcwBuilder
        EXAMPLES_VALID = [
            {'radius': '1.0', 'zb': '1.0', 'ze': '2.0'},
            {'radius': 1.0, 'zb': 1.0, 'ze': 2.0},
            {'radius': _utils.REAL, 'zb': _utils.REAL, 'ze': pymcnp.utils.types.Real(2.0)},
        ]
        EXAMPLES_INVALID = [
            {'radius': None, 'zb': '1.0', 'ze': '2.0'},
            {'radius': '1.0', 'zb': None, 'ze': '2.0'},
            {'radius': '1.0', 'zb': '1.0', 'ze': None},
        ]
