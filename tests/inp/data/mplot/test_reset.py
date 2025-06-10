import pymcnp
from .... import _utils


class Test_Reset:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Reset
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ResetBuilder
        EXAMPLES_VALID = [{'aa': 'all'}, {'aa': pymcnp.utils.types.String('all')}, {'aa': None}]
        EXAMPLES_INVALID = [{'aa': 'hello'}]
