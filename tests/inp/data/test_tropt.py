import pymcnp
from ... import _utils


class Test_Tropt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tropt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.TroptBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.tropt.ELOSS]}, {'options': [_utils.builder.inp.data.tropt.ELOSS]}, {'options': [_utils.ast.inp.data.tropt.ELOSS]}, {'options': None}]
        EXAMPLES_INVALID = []
