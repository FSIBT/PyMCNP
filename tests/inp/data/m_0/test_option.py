import pymcnp
from .... import _utils


class Test_Gas:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Gas
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.GasBuilder
        EXAMPLES_VALID = [{'setting': 'yes'}, {'setting': pymcnp.utils.types.String('yes')}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Estep:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Estep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.EstepBuilder
        EXAMPLES_VALID = [{'step': '1'}, {'step': 1}, {'step': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'step': None}]


class Test_Hstep:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Hstep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.HstepBuilder
        EXAMPLES_VALID = [{'step': '1'}, {'step': 1}, {'step': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'step': None}]


class Test_Nlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Nlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.NlibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Plib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Plib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.PlibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Pnlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Pnlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.PnlibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Elib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Elib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.ElibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Hlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Hlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.HlibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Alib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Alib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.AlibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Slib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Slib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.SlibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Tlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Tlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.TlibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Dlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Dlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.DlibBuilder
        EXAMPLES_VALID = [{'abx': 'a'}, {'abx': 'a'}, {'abx': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'abx': None}]


class Test_Cond:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Cond
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.CondBuilder
        EXAMPLES_VALID = [{'setting': '1.0'}, {'setting': 1.0}, {'setting': _utils.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Refi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Refi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.RefiBuilder
        EXAMPLES_VALID = [
            {'refractive_index': '1.0'},
            {'refractive_index': 1.0},
            {'refractive_index': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'refractive_index': None}]


class Test_Refc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Refc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.RefcBuilder
        EXAMPLES_VALID = [
            {'coefficents': ['1.0']},
            {'coefficents': [1.0]},
            {'coefficents': [_utils.REAL]},
        ]
        EXAMPLES_INVALID = [{'coefficents': None}]


class Test_Refs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Refs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.RefsBuilder
        EXAMPLES_VALID = [
            {'coefficents': ['1.0']},
            {'coefficents': [1.0]},
            {'coefficents': [_utils.REAL]},
        ]
        EXAMPLES_INVALID = [{'coefficents': None}]
