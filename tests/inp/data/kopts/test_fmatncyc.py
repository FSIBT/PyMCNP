import pymcnp
from .... import _utils


class Test_Fmatncyc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatncyc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatncycBuilder
        EXAMPLES_VALID = [{'fmat_ncyc': _utils.string.type.REAL}, {'fmat_ncyc': 3.1}, {'fmat_ncyc': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_ncyc': None}]
