import pymcnp
from .... import _utils


class Test_Pty:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssw.Pty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ssw.PtyBuilder
        EXAMPLES_VALID = [{'tracks': [_utils.string.type.DESIGNATOR]}, {'tracks': [_utils.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'tracks': None}]
