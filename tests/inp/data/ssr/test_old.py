import pymcnp
from .... import _utils


class Test_Old:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Old
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.OldBuilder
        EXAMPLES_VALID = [{'numbers': [_utils.string.type.INTEGER]}, {'numbers': [1]}, {'numbers': [_utils.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]
