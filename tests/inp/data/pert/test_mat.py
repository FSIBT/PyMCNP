import pymcnp
from .... import _utils


class Test_Mat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.MatBuilder
        EXAMPLES_VALID = [{'material': _utils.string.type.INTEGER}, {'material': 1}, {'material': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'material': None}]
