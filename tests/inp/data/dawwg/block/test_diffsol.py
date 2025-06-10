import pymcnp
from ..... import _utils


class Test_Diffsol:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Diffsol
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.DiffsolBuilder
        EXAMPLES_VALID = [{'setting': _utils.string.type.STRING}, {'setting': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]
