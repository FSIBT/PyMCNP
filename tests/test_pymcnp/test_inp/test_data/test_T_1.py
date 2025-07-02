import pymcnp
from .... import consts
from .... import classes


class Test_T_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.T_1
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.t_1.CBEG]}]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.ast.inp.data.t_1.CBEG]}, {'suffix': consts.ast.type.INTEGER, 'options': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.T_1
        EXAMPLES_VALID = [consts.string.inp.data.T_1]
        EXAMPLES_INVALID = ['hello']


class Test_TBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.TBuilder_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'options': [consts.string.inp.data.t_1.CBEG]},
            {'suffix': 1, 'options': [consts.builder.inp.data.t_1.CBEG]},
            {'suffix': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.t_1.CBEG]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.string.inp.data.t_1.CBEG]}, {'suffix': consts.string.type.INTEGER, 'options': None}]
