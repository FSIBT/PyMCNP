import pymcnp
from ... import _utils


class Test_Mt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.MtBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'identifiers': [_utils.string.type.STRING]},
            {'suffix': 1, 'identifiers': [_utils.string.type.STRING]},
            {'suffix': _utils.ast.type.INTEGER, 'identifiers': [_utils.ast.type.STRING]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'identifiers': [_utils.string.type.STRING]}, {'suffix': _utils.string.type.INTEGER, 'identifiers': None}]
