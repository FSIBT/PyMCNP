import pymcnp
from .... import _utils


class Test_Geom:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Geom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.GeomBuilder
        EXAMPLES_VALID = [
            {'geometry': 'rpt'},
            {'geometry': pymcnp.utils.types.String('rpt')},
        ]
        EXAMPLES_INVALID = [{'geometry': None}]


class Test_Ref:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Ref
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.RefBuilder
        EXAMPLES_VALID = [{'point': ['1.0']}, {'point': [1.0]}, {'point': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]


class Test_Origin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Origin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.OriginBuilder
        EXAMPLES_VALID = [{'point': ['1.0']}, {'point': [1.0]}, {'point': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]


class Test_Axs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.AxsBuilder
        EXAMPLES_VALID = [{'vector': ['1.0']}, {'vector': [1.0]}, {'vector': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]


class Test_Vec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.VecBuilder
        EXAMPLES_VALID = [{'vector': ['1.0']}, {'vector': [1.0]}, {'vector': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]


class Test_Imesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Imesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.ImeshBuilder
        EXAMPLES_VALID = [{'vector': ['1.0']}, {'vector': [1.0]}, {'vector': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]


class Test_Iints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Iints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.IintsBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Jmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Jmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.JmeshBuilder
        EXAMPLES_VALID = [{'vector': ['1.0']}, {'vector': [1.0]}, {'vector': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]


class Test_Jints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Jints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.JintsBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Kmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Kmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.KmeshBuilder
        EXAMPLES_VALID = [{'vector': ['1.0']}, {'vector': [1.0]}, {'vector': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]


class Test_Kints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Kints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.KintsBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]
