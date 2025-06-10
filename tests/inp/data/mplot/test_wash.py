import pymcnp
from .... import _utils


class Test_Wash:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Wash
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.WashBuilder
        EXAMPLES_VALID = [{'aa': 'off'}, {'aa': pymcnp.utils.types.String('off')}]
        EXAMPLES_INVALID = [{'aa': None}, {'aa': 'hello'}]
