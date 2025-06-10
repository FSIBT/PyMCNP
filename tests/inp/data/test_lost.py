import pymcnp
from ... import _utils


class Test_Lost:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lost
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.LostBuilder
        EXAMPLES_VALID = [{'lost1': _utils.string.type.INTEGER, 'lost2': _utils.string.type.INTEGER}, {'lost1': 1, 'lost2': 1}, {'lost1': _utils.ast.type.INTEGER, 'lost2': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'lost1': None, 'lost2': _utils.string.type.INTEGER}, {'lost1': _utils.string.type.INTEGER, 'lost2': None}]
