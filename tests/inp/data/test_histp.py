import pymcnp
from ... import _utils


class Test_Histp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Histp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.HistpBuilder
        EXAMPLES_VALID = [
            {'lhist': _utils.string.type.INTEGER, 'cells': [_utils.string.type.INTEGER]},
            {'lhist': 1, 'cells': [1]},
            {'lhist': _utils.ast.type.INTEGER, 'cells': [_utils.ast.type.INTEGER]},
            {'lhist': None, 'cells': [_utils.string.type.INTEGER]},
            {'lhist': _utils.string.type.INTEGER, 'cells': None},
        ]
        EXAMPLES_INVALID = []
