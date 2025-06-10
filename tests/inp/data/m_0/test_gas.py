import pymcnp
from .... import _utils


class Test_Gas:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Gas
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.m_0.GasBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.utils.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
