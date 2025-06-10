import pymcnp
from .... import _utils


class Test_Ksental:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Ksental
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.KsentalBuilder
        EXAMPLES_VALID = [{'fileopt': 'mctal'}, {'fileopt': pymcnp.utils.types.String('mctal')}]
        EXAMPLES_INVALID = [{'fileopt': None}, {'fileopt': 'hello'}]
