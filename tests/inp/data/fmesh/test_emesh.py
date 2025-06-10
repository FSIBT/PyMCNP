import pymcnp
from .... import _utils


class Test_Emesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Emesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.EmeshBuilder
        EXAMPLES_VALID = [{'energy': _utils.string.type.REAL}, {'energy': 3.1}, {'energy': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]
