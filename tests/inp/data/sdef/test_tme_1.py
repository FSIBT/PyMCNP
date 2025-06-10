import pymcnp
from .... import _utils


class Test_Tme_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tme_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.TmeBuilder_1
        EXAMPLES_VALID = [{'time': _utils.string.type.EMBEDDEDDISTRIBUTIONNUMBER}, {'time': _utils.ast.type.EMBEDDEDDISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'time': None}]
