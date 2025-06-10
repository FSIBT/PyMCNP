import pymcnp
from .... import _utils


class Test_Sfyield:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Sfyield
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.SfyieldBuilder
        EXAMPLES_VALID = [{'fission_yield': _utils.string.type.REAL}, {'fission_yield': 3.1}, {'fission_yield': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fission_yield': None}]
