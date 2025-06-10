import pymcnp
from ... import _utils


class Test_Ssr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ssr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SsrBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.ssr.AXS]}, {'options': [_utils.builder.inp.data.ssr.AXS]}, {'options': [_utils.ast.inp.data.ssr.AXS]}, {'options': None}]
        EXAMPLES_INVALID = []
