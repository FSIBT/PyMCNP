import pymcnp
from .... import _utils


class Test_Conic:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Conic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.ConicBuilder
        EXAMPLES_VALID = [{'setting': 'col'}, {'setting': pymcnp.utils.types.String('col')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
