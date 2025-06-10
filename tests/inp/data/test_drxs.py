import pymcnp
from ... import _utils


class Test_Drxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Drxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.DrxsBuilder
        EXAMPLES_VALID = [{'zaids': [_utils.string.type.ZAID]}, {'zaids': [_utils.ast.type.ZAID]}, {'zaids': None}]
        EXAMPLES_INVALID = []
