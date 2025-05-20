import pymcnp
from .... import _utils


class Test_Cel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.CelBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Sur:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Sur
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.SurBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Erg_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Erg_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.ErgBuilder_0
        EXAMPLES_VALID = [{'energy': '1.0'}, {'energy': 1.0}, {'energy': _utils.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]


class Test_Erg_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Erg_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.ErgBuilder_1
        EXAMPLES_VALID = [{'energy': 'd10'}, {'energy': _utils.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'energy': None}]


class Test_Tme_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tme_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.TmeBuilder_0
        EXAMPLES_VALID = [{'time': '1.0'}, {'time': 1.0}, {'time': _utils.REAL}]
        EXAMPLES_INVALID = [{'time': None}]


class Test_Tme_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tme_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.TmeBuilder_1
        EXAMPLES_VALID = [{'time': 'd2 > d1'}, {'time': _utils.EMBEDDED_DISTRIBUTION}]
        EXAMPLES_INVALID = [{'time': None}]


class Test_Dir_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dir_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.DirBuilder_0
        EXAMPLES_VALID = [
            {'cosine': None},
            {'cosine': '1.0'},
            {'cosine': 1.0},
            {'cosine': _utils.REAL},
        ]
        EXAMPLES_INVALID = []


class Test_Dir_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dir_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.DirBuilder_1
        EXAMPLES_VALID = [{'cosine': None}, {'cosine': 'd1'}, {'cosine': _utils.DISTRIBUTION}]
        EXAMPLES_INVALID = []


class Test_Vec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.VecBuilder
        EXAMPLES_VALID = [
            {'x': '1.0', 'y': '1.0', 'z': '1.0'},
            {'x': 1.0, 'y': 1.0, 'z': 1.0},
            {'x': _utils.REAL, 'y': _utils.REAL, 'z': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '1.0', 'z': '1.0'},
            {'x': '1.0', 'y': None, 'z': '1.0'},
            {'x': '1.0', 'y': '1.0', 'z': None},
        ]


class Test_Nrm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Nrm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.NrmBuilder
        EXAMPLES_VALID = [{'sign': '1'}, {'sign': 1}, {'sign': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'sign': None}]


class Test_Pos:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Pos
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.PosBuilder
        EXAMPLES_VALID = [{'vector': ['1.0']}, {'vector': [1.0]}, {'vector': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]


class Test_Rad_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Rad_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.RadBuilder_0
        EXAMPLES_VALID = [
            {'radial_distance': '1.0'},
            {'radial_distance': 1.0},
            {'radial_distance': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'radial_distance': None}]


class Test_Rad_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Rad_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.RadBuilder_1
        EXAMPLES_VALID = [
            {'radial_distance': 'd1'},
            {'radial_distance': _utils.DISTRIBUTION},
        ]
        EXAMPLES_INVALID = [{'radial_distance': None}]


class Test_Ext:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.ExtBuilder
        EXAMPLES_VALID = [
            {'distance_cosine': '1.0'},
            {'distance_cosine': 1.0},
            {'distance_cosine': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'distance_cosine': None}]


class Test_Axs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.AxsBuilder
        EXAMPLES_VALID = [
            {'x': '1.0', 'y': '1.0', 'z': '1.0'},
            {'x': 1.0, 'y': 1.0, 'z': 1.0},
            {'x': _utils.REAL, 'y': _utils.REAL, 'z': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '1.0', 'z': '1.0'},
            {'x': '1.0', 'y': None, 'z': '1.0'},
            {'x': '1.0', 'y': '1.0', 'z': None},
        ]


class Test_X:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.X
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.XBuilder
        EXAMPLES_VALID = [
            {'x_coordinate': '1.0'},
            {'x_coordinate': 1.0},
            {'x_coordinate': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'x_coordinate': None}]


class Test_Y:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.YBuilder
        EXAMPLES_VALID = [
            {'y_coordinate': '1.0'},
            {'y_coordinate': 1.0},
            {'y_coordinate': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'y_coordinate': None}]


class Test_Z:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.ZBuilder
        EXAMPLES_VALID = [
            {'z_coordinate': '1.0'},
            {'z_coordinate': 1.0},
            {'z_coordinate': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'z_coordinate': None}]


class Test_Ccc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Ccc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.CccBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Ara:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Ara
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.AraBuilder
        EXAMPLES_VALID = [{'area': '1.0'}, {'area': 1.0}, {'area': _utils.REAL}]
        EXAMPLES_INVALID = [{'area': None}]


class Test_Wgt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Wgt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.WgtBuilder
        EXAMPLES_VALID = [{'weight': '1.0'}, {'weight': 1.0}, {'weight': _utils.REAL}]
        EXAMPLES_INVALID = [{'weight': None}]


class Test_Tr_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tr_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.TrBuilder_0
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Tr_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tr_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.TrBuilder_1
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Eff:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Eff
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.EffBuilder
        EXAMPLES_VALID = [{'criterion': '1.0'}, {'criterion': 1.0}, {'criterion': _utils.REAL}]
        EXAMPLES_INVALID = [{'criterion': None}]


class Test_Par:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Par
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.ParBuilder
        EXAMPLES_VALID = [{'kind': 'a'}, {'kind': 'a'}, {'kind': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'kind': None}]


class Test_Dat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.DatBuilder
        EXAMPLES_VALID = [
            {'month': '1', 'day': '1', 'year': '1'},
            {'month': 1, 'day': 1, 'year': 1},
            {'month': _utils.INTEGER, 'day': _utils.INTEGER, 'year': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'month': None, 'day': '1', 'year': '1'},
            {'month': '1', 'day': None, 'year': '1'},
            {'month': '1', 'day': '1', 'year': None},
        ]


class Test_Loc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Loc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.LocBuilder
        EXAMPLES_VALID = [
            {'latitude': '1.0', 'longitude': '1.0', 'altitude': '1.0'},
            {'latitude': 1.0, 'longitude': 1.0, 'altitude': 1.0},
            {'latitude': _utils.REAL, 'longitude': _utils.REAL, 'altitude': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'latitude': None, 'longitude': '1.0', 'altitude': '1.0'},
            {'latitude': '1.0', 'longitude': None, 'altitude': '1.0'},
            {'latitude': '1.0', 'longitude': '1.0', 'altitude': None},
        ]


class Test_Bem:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Bem
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.BemBuilder
        EXAMPLES_VALID = [
            {'exn': '1.0', 'eyn': '1.0', 'bml': '1.0'},
            {'exn': 1.0, 'eyn': 1.0, 'bml': 1.0},
            {'exn': _utils.REAL, 'eyn': _utils.REAL, 'bml': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'exn': None, 'eyn': '1.0', 'bml': '1.0'},
            {'exn': '1.0', 'eyn': None, 'bml': '1.0'},
            {'exn': '1.0', 'eyn': '1.0', 'bml': None},
        ]


class Test_Bap:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Bap
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.BapBuilder
        EXAMPLES_VALID = [
            {'ba1': '1.0', 'ba2': '1.0', 'u': '1.0'},
            {'ba1': 1.0, 'ba2': 1.0, 'u': 1.0},
            {'ba1': _utils.REAL, 'ba2': _utils.REAL, 'u': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'ba1': None, 'ba2': '1.0', 'u': '1.0'},
            {'ba1': '1.0', 'ba2': None, 'u': '1.0'},
            {'ba1': '1.0', 'ba2': '1.0', 'u': None},
        ]
