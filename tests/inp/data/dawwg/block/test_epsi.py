import pymcnp
from ..... import _utils


class Test_Epsi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Epsi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.EpsiBuilder
        EXAMPLES_VALID = [{'setting': _utils.string.type.REAL}, {'setting': 3.1}, {'setting': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]
