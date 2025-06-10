import pymcnp
from .... import _utils


class Test_Write:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Write
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.WriteBuilder
        EXAMPLES_VALID = [{'setting': 'all'}, {'setting': pymcnp.utils.types.String('all')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
