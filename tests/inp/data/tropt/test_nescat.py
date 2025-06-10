import pymcnp
from .... import _utils


class Test_Nescat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Nescat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.tropt.NescatBuilder
        EXAMPLES_VALID = [{'setting': 'off'}, {'setting': pymcnp.utils.types.String('off')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
