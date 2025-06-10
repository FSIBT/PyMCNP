import pymcnp
from ... import _utils


class Test_Mode:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mode
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ModeBuilder
        EXAMPLES_VALID = [{'particles': [_utils.string.type.DESIGNATOR]}, {'particles': [_utils.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]
