import pymcnp
from .... import _utils


class Test_Imesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Imesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.ImeshBuilder
        EXAMPLES_VALID = [{'vector': [_utils.string.type.REAL]}, {'vector': [3.1]}, {'vector': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]
