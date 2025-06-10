import pymcnp
from .... import _utils


class Test_Matcell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Matcell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.MatcellBuilder
        EXAMPLES_VALID = [{'pairs': [_utils.string.type.MATCELL]}, {'pairs': [_utils.ast.type.MATCELL]}]
        EXAMPLES_INVALID = [{'pairs': None}]
