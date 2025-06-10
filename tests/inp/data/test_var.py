import pymcnp
from ... import _utils


class Test_Var:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Var
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.VarBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.var.RR]}, {'options': [_utils.builder.inp.data.var.RR]}, {'options': [_utils.ast.inp.data.var.RR]}, {'options': None}]
        EXAMPLES_INVALID = []
