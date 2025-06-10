import pymcnp
from .... import _utils


class Test_Sfnu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Sfnu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmult.SfnuBuilder
        EXAMPLES_VALID = [{'distribution': [_utils.string.type.REAL]}, {'distribution': [3.1]}, {'distribution': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'distribution': None}]
