import pymcnp
from .... import _utils


class Test_Label:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Label
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LabelBuilder
        EXAMPLES_VALID = [{'aa': _utils.string.type.STRING}, {'aa': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'aa': None}]
