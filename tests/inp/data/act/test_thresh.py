import pymcnp
from .... import _utils


class Test_Thresh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Thresh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.ThreshBuilder
        EXAMPLES_VALID = [{'fraction': '0.8'}, {'fraction': 0.8}, {'fraction': pymcnp.utils.types.Real(0.8)}]
        EXAMPLES_INVALID = [{'fraction': None}, {'fraction': '3.1'}]
