import pymcnp
from .... import _utils


class Test_Ext:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssr.ExtBuilder
        EXAMPLES_VALID = [{'number': _utils.string.type.DISTRIBUTIONNUMBER}, {'number': _utils.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'number': None}]
