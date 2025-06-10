import pymcnp
from .... import _utils


class Test_Points:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.Points
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.PointsBuilder
        EXAMPLES_VALID = [{'name': _utils.string.type.STRING}, {'name': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'name': None}]
