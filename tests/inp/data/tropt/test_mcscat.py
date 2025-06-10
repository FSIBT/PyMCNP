import pymcnp
from .... import _utils


class Test_Mcscat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Mcscat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.tropt.McscatBuilder
        EXAMPLES_VALID = [{'setting': 'off'}, {'setting': pymcnp.utils.types.String('off')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
