import pymcnp
from .... import _utils


class Test_Fmatnz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatnz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatnzBuilder
        EXAMPLES_VALID = [{'fmat_nz': _utils.string.type.REAL}, {'fmat_nz': 3.1}, {'fmat_nz': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_nz': None}]
