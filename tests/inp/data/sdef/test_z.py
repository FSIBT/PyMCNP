import pymcnp
from .... import _utils


class Test_Z:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.ZBuilder
        EXAMPLES_VALID = [{'z_coordinate': _utils.string.type.REAL}, {'z_coordinate': 3.1}, {'z_coordinate': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'z_coordinate': None}]
