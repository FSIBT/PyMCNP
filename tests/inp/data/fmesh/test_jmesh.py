import pymcnp
from .... import _utils


class Test_Jmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Jmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.JmeshBuilder
        EXAMPLES_VALID = [{'locations': [_utils.string.type.REAL]}, {'locations': [3.1]}, {'locations': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'locations': None}]
