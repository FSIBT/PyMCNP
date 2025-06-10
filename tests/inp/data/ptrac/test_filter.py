import pymcnp
from .... import _utils


class Test_Filter:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Filter
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.FilterBuilder
        EXAMPLES_VALID = [{'variables': [_utils.string.type.PTRACFILTER]}, {'variables': [_utils.ast.type.PTRACFILTER]}]
        EXAMPLES_INVALID = [{'variables': None}]
