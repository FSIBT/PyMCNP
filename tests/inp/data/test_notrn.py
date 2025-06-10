import pymcnp
from ... import _utils


class Test_Notrn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Notrn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.NotrnBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
