import pymcnp
from .... import _utils


class Test_Rad_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Rad_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.RadBuilder_1
        EXAMPLES_VALID = [{'radial_distance': _utils.string.type.DISTRIBUTIONNUMBER}, {'radial_distance': _utils.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'radial_distance': None}]
