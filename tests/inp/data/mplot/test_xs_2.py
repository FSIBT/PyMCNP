import pymcnp
from .... import _utils


class Test_Xs_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XsBuilder_2
        EXAMPLES_VALID = [{'m': '?'}, {'m': pymcnp.utils.types.String('?')}]
        EXAMPLES_INVALID = [{'m': None}, {'m': 'hello'}]
