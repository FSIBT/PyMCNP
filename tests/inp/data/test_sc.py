import pymcnp
from ... import _utils


class Test_Sc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ScBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'comment': [_utils.string.type.STRING]},
            {'suffix': 1, 'comment': [_utils.string.type.STRING]},
            {'suffix': _utils.ast.type.INTEGER, 'comment': [_utils.ast.type.STRING]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'comment': [_utils.string.type.STRING]}, {'suffix': _utils.string.type.INTEGER, 'comment': None}]
