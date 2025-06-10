import pymcnp
from .... import _utils


class Test_Fmatskpt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatskpt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatskptBuilder
        EXAMPLES_VALID = [{'fmat_skip': _utils.string.type.REAL}, {'fmat_skip': 3.1}, {'fmat_skip': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_skip': None}]
