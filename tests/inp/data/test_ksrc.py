import pymcnp
from ... import _utils


class Test_Ksrc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ksrc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.KsrcBuilder
        EXAMPLES_VALID = [{'locations': [_utils.string.type.LOCATION]}, {'locations': [_utils.ast.type.LOCATION]}]
        EXAMPLES_INVALID = [{'locations': None}]
