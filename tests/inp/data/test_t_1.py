import pymcnp
from ... import _utils


class Test_T_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.T_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.TBuilder_1
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'options': [_utils.string.inp.data.t_1.CBEG]},
            {'suffix': 1, 'options': [_utils.builder.inp.data.t_1.CBEG]},
            {'suffix': _utils.ast.type.INTEGER, 'options': [_utils.ast.inp.data.t_1.CBEG]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [_utils.string.inp.data.t_1.CBEG]}, {'suffix': _utils.string.type.INTEGER, 'options': None}]
