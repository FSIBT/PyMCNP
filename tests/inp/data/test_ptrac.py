import pymcnp
from ... import _utils


class Test_Ptrac:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ptrac
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.PtracBuilder
        EXAMPLES_VALID = [{'options': [_utils.string.inp.data.ptrac.BUFFER]}, {'options': [_utils.builder.inp.data.ptrac.BUFFER]}, {'options': [_utils.ast.inp.data.ptrac.BUFFER]}, {'options': None}]
        EXAMPLES_INVALID = []
