import pymcnp
from .... import _utils


class Test_Fmatnx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatnx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatnxBuilder
        EXAMPLES_VALID = [{'fmat_nx': _utils.string.type.REAL}, {'fmat_nx': 3.1}, {'fmat_nx': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_nx': None}]
