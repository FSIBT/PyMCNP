import pymcnp
from .... import _utils


class Test_Dg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.DgBuilder
        EXAMPLES_VALID = [{'source': _utils.string.type.STRING}, {'source': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'source': None}]
