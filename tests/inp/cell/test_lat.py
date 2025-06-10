import pymcnp
from ... import _utils


class Test_Lat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Lat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.LatBuilder
        EXAMPLES_VALID = [{'shape': _utils.string.type.INTEGER}, {'shape': 1}, {'shape': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'shape': None}]
