import pymcnp
from ..... import _utils


class Test_Ngroup:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ngroup
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NgroupBuilder
        EXAMPLES_VALID = [{'value': _utils.string.type.INTEGER}, {'value': 1}, {'value': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'value': None}]
