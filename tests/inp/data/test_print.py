import pymcnp
from ... import _utils


class Test_Print:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Print
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.PrintBuilder
        EXAMPLES_VALID = [{'tables': [_utils.string.type.INTEGER]}, {'tables': [1]}, {'tables': [_utils.ast.type.INTEGER]}, {'tables': None}]
        EXAMPLES_INVALID = []
