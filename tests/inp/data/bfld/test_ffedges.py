import pymcnp
from .... import _utils


class Test_Ffedges:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Ffedges
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.FfedgesBuilder
        EXAMPLES_VALID = [{'numbers': [_utils.string.type.REAL]}, {'numbers': [3.1]}, {'numbers': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'numbers': None}]
