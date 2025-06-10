import pymcnp
from .... import _utils


class Test_Block:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.Block
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.BlockBuilder
        EXAMPLES_VALID = [
            {'setting': _utils.string.type.INTEGER, 'options': [_utils.string.inp.data.dawwg.block.AJED]},
            {'setting': 1, 'options': [_utils.builder.inp.data.dawwg.block.AJED]},
            {'setting': _utils.ast.type.INTEGER, 'options': [_utils.ast.inp.data.dawwg.block.AJED]},
            {'setting': _utils.string.type.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [{'setting': None, 'options': [_utils.string.inp.data.dawwg.block.AJED]}]
