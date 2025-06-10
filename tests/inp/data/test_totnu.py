import pymcnp
from ... import _utils


class Test_Totnu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Totnu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.TotnuBuilder
        EXAMPLES_VALID = [{'no': 'no'}, {'no': pymcnp.utils.types.String('no')}, {'no': None}]
        EXAMPLES_INVALID = [{'no': 'hello'}]
