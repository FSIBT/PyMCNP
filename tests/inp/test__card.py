import pymcnp
from .. import _utils


class Test_Card:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Card
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []
