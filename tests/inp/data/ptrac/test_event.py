import pymcnp
from .... import _utils


class Test_Event:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Event
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.EventBuilder
        EXAMPLES_VALID = [{'settings': [_utils.string.type.STRING]}, {'settings': [_utils.ast.type.STRING]}]
        EXAMPLES_INVALID = [{'settings': None}]
