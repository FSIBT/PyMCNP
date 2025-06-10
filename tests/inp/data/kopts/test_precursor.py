import pymcnp
from .... import _utils


class Test_Precursor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Precursor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.PrecursorBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.utils.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
