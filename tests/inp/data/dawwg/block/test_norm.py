import pymcnp
from ..... import _utils


class Test_Norm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Norm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NormBuilder
        EXAMPLES_VALID = [{'setting': _utils.string.type.REAL}, {'setting': 3.1}, {'setting': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]
