import pymcnp
from .. import _utils


class Test_Option:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Option
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = [
            'hello',
        ]
