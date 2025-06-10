import pymcnp
from .... import _utils


class Test_Type:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Type
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.TypeBuilder
        EXAMPLES_VALID = [{'setting': 'flux'}, {'setting': pymcnp.utils.types.String('flux')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
