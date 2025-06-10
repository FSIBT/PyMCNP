import pymcnp
from .... import _utils


class Test_Sample:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Sample
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.SampleBuilder
        EXAMPLES_VALID = [{'setting': 'correlate'}, {'setting': pymcnp.utils.types.String('correlate')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
