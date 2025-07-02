import pymcnp
from ..... import consts
from ..... import classes


class Test_Block:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.Block
        EXAMPLES_VALID = [{'setting': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.dawwg.block.AJED]}, {'setting': consts.ast.type.INTEGER, 'options': None}]
        EXAMPLES_INVALID = [{'setting': None, 'options': [consts.ast.inp.data.dawwg.block.AJED]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.Block
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.BLOCK]
        EXAMPLES_INVALID = ['hello']


class Test_BlockBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.BlockBuilder
        EXAMPLES_VALID = [
            {'setting': consts.string.type.INTEGER, 'options': [consts.string.inp.data.dawwg.block.AJED]},
            {'setting': 1, 'options': [consts.builder.inp.data.dawwg.block.AJED]},
            {'setting': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.dawwg.block.AJED]},
            {'setting': consts.string.type.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [{'setting': None, 'options': [consts.string.inp.data.dawwg.block.AJED]}]
