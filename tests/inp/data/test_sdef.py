import pymcnp
from ... import _utils


class Test_Sdef:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sdef
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SdefBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.sdef.ARA]}, {'options': [_utils.builder.inp.data.sdef.ARA]}, {'options': [_utils.ast.inp.data.sdef.ARA]}, {'options': None}]
        EXAMPLES_INVALID = []
