import pymcnp
from .... import _utils


class Test_Axs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.AxsBuilder
        EXAMPLES_VALID = [{'cosines': [_utils.string.type.REAL]}, {'cosines': [3.1]}, {'cosines': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'cosines': None}]
