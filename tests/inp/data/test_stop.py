import pymcnp
from ... import _utils


class Test_Stop:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Stop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.StopBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.stop.CTME]}, {'options': [_utils.builder.inp.data.stop.CTME]}, {'options': [_utils.ast.inp.data.stop.CTME]}, {'options': None}]
        EXAMPLES_INVALID = []
