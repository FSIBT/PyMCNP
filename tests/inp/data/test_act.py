import pymcnp
from ... import _utils


class Test_Act:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Act
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ActBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.act.DG]}, {'options': [_utils.builder.inp.data.act.DG]}, {'options': [_utils.ast.inp.data.act.DG]}, {'options': None}]
        EXAMPLES_INVALID = []
