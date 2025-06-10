import pymcnp
from ... import _utils


class Test_Area:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Area
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.AreaBuilder
        EXAMPLES_VALID = [{'areas': [_utils.string.type.REAL]}, {'areas': [3.1]}, {'areas': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'areas': None}]
