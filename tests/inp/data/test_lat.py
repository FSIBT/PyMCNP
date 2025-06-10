import pymcnp
from ... import _utils


class Test_Lat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.LatBuilder
        EXAMPLES_VALID = [{'type': [_utils.string.type.INTEGER]}, {'type': [1]}, {'type': [_utils.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'type': None}]
