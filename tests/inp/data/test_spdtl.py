import pymcnp
from ... import _utils


class Test_Spdtl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Spdtl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SpdtlBuilder
        EXAMPLES_VALID = [{'keyword': _utils.string.type.STRING}, {'keyword': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'keyword': None}]
