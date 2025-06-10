import pymcnp
from .... import _utils


class Test_Inc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Inc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.IncBuilder
        EXAMPLES_VALID = [
            {'lower': _utils.string.type.REAL, 'upper': _utils.string.type.REAL},
            {'lower': 3.1, 'upper': 3.1},
            {'lower': _utils.ast.type.REAL, 'upper': _utils.ast.type.REAL},
            {'lower': _utils.string.type.REAL, 'upper': None},
        ]
        EXAMPLES_INVALID = [{'lower': None, 'upper': _utils.string.type.REAL}]
