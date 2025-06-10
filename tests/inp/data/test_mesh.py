import pymcnp
from ... import _utils


class Test_Mesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.MeshBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.mesh.AXS]}, {'options': [_utils.builder.inp.data.mesh.AXS]}, {'options': [_utils.ast.inp.data.mesh.AXS]}, {'options': None}]
        EXAMPLES_INVALID = []
