import pymcnp
from .... import _utils


class Test_Buffer:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Buffer
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.BufferBuilder
        EXAMPLES_VALID = [{'storage': '1'}, {'storage': 1}, {'storage': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'storage': None}]


class Test_File:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.File
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.FileBuilder
        EXAMPLES_VALID = [
            {'setting': 'asc'},
            {'setting': pymcnp.utils.types.String('asc')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Max:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Max
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.MaxBuilder
        EXAMPLES_VALID = [{'events': '1'}, {'events': 1}, {'events': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'events': None}]


class Test_Meph:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Meph
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.MephBuilder
        EXAMPLES_VALID = [{'events': '1'}, {'events': 1}, {'events': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'events': None}]


class Test_Write:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Write
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.WriteBuilder
        EXAMPLES_VALID = [
            {'setting': 'pos'},
            {'setting': pymcnp.utils.types.String('pos')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Conic:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Conic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.ConicBuilder
        EXAMPLES_VALID = [
            {'setting': 'lin'},
            {'setting': pymcnp.utils.types.String('lin')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Event:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Event
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.EventBuilder
        EXAMPLES_VALID = [{'settings': ['a']}, {'settings': [_utils.STRING]}]
        EXAMPLES_INVALID = [{'settings': None}]


class Test_Filter:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Filter
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.FilterBuilder
        EXAMPLES_VALID = [{'variables': ['1,a']}, {'variables': [_utils.FILTER]}]
        EXAMPLES_INVALID = [{'variables': None}]


class Test_Type:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Type
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.TypeBuilder
        EXAMPLES_VALID = [{'particles': ['n']}, {'particles': [_utils.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]


class Test_Nps:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.NpsBuilder
        EXAMPLES_VALID = [{'particles': ['1']}, {'particles': [1]}, {'particles': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'particles': None}]


class Test_Cell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.CellBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Surface:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Surface
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.SurfaceBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Tally:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Tally
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.TallyBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Value:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Value
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.ValueBuilder
        EXAMPLES_VALID = [{'cutoff': '1.0'}, {'cutoff': 1.0}, {'cutoff': _utils.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]
