import pymcnp
from .... import _utils


class Test_Dn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.DnBuilder
        EXAMPLES_VALID = [{'source': 'model'}, {'source': pymcnp.utils.types.String('model')}]
        EXAMPLES_INVALID = [{'source': None}, {'source': 'hello'}]
