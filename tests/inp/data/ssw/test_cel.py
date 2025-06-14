import pymcnp
from .... import _utils


class Test_Cel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssw.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssw.CelBuilder
        EXAMPLES_VALID = [{'cfs': [_utils.string.type.INTEGER]}, {'cfs': [1]}, {'cfs': [_utils.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'cfs': None}]
