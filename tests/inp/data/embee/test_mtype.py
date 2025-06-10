import pymcnp
from .... import _utils


class Test_Mtype:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Mtype
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.MtypeBuilder
        EXAMPLES_VALID = [{'kind': 'flux'}, {'kind': pymcnp.utils.types.String('flux')}]
        EXAMPLES_INVALID = [{'kind': None}, {'kind': 'hello'}]
