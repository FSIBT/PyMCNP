import pymcnp
from .... import _utils


class Test_Iso:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Iso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.IsoBuilder
        EXAMPLES_VALID = [{'zaids': [_utils.string.type.ZAID]}, {'zaids': [_utils.ast.type.ZAID]}]
        EXAMPLES_INVALID = [{'zaids': None}]
