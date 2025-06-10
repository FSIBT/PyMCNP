import pymcnp
from .... import _utils


class Test_Fmatny:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatny
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatnyBuilder
        EXAMPLES_VALID = [{'fmat_ny': _utils.string.type.REAL}, {'fmat_ny': 3.1}, {'fmat_ny': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_ny': None}]
