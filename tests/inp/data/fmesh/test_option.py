import pymcnp
from .... import _utils


class Test_Geom:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Geom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.GeomBuilder
        EXAMPLES_VALID = [
            {'geometry': 'xyz'},
            {'geometry': pymcnp.utils.types.String('xyz')},
        ]
        EXAMPLES_INVALID = [{'geometry': None}]


class Test_Origin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Origin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.OriginBuilder
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


class Test_Axs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.AxsBuilder
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


class Test_Vec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.VecBuilder
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


class Test_Imesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Imesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.ImeshBuilder
        EXAMPLES_VALID = [{'locations': '1.0'}, {'locations': 1.0}, {'locations': _utils.REAL}]
        EXAMPLES_INVALID = [{'locations': None}]


class Test_Iints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Iints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.IintsBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Jmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Jmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.JmeshBuilder
        EXAMPLES_VALID = [{'locations': '1.0'}, {'locations': 1.0}, {'locations': _utils.REAL}]
        EXAMPLES_INVALID = [{'locations': None}]


class Test_Jints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Jints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.JintsBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Kmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Kmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.KmeshBuilder
        EXAMPLES_VALID = [{'locations': '1.0'}, {'locations': 1.0}, {'locations': _utils.REAL}]
        EXAMPLES_INVALID = [{'locations': None}]


class Test_Kints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Kints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.KintsBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Emesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Emesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.EmeshBuilder
        EXAMPLES_VALID = [{'energy': '1.0'}, {'energy': 1.0}, {'energy': _utils.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]


class Test_Eints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Eints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.EintsBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Enorm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Enorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.EnormBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Tmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Tmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.TmeshBuilder
        EXAMPLES_VALID = [{'time': '1.0'}, {'time': 1.0}, {'time': _utils.REAL}]
        EXAMPLES_INVALID = [{'time': None}]


class Test_Tints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Tints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.TintsBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Tnorm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Tnorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.TnormBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Factor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.FactorBuilder
        EXAMPLES_VALID = [{'multiple': '1.0'}, {'multiple': 1.0}, {'multiple': _utils.REAL}]
        EXAMPLES_INVALID = [{'multiple': None}]


class Test_Out:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Out
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.OutBuilder
        EXAMPLES_VALID = [
            {'setting': 'cf'},
            {'setting': pymcnp.utils.types.String('cf')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Tr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Tr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.TrBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Inc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Inc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.IncBuilder
        EXAMPLES_VALID = [
            {'lower': '1.0', 'upper': '1.0'},
            {'lower': '1.0', 'upper': None},
            {'lower': 1.0, 'upper': 1.0},
            {'lower': _utils.REAL, 'upper': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'lower': None, 'upper': '1.0'}]


class Test_Type:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Type
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.TypeBuilder
        EXAMPLES_VALID = [
            {'setting': 'flux'},
            {'setting': pymcnp.utils.types.String('flux')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Kclear:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Kclear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.KclearBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]
