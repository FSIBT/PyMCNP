import pymcnp
from .... import _utils


class Test_Fmatspace:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatspace
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatspaceBuilder
        EXAMPLES_VALID = [{'fmat_space': _utils.string.type.REAL}, {'fmat_space': 3.1}, {'fmat_space': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_space': None}]
