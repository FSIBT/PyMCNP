import pymcnp
from .... import _utils


class Test_Rad_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Rad_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.RadBuilder_0
        EXAMPLES_VALID = [{'radial_distance': _utils.string.type.REAL}, {'radial_distance': 3.1}, {'radial_distance': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'radial_distance': None}]
