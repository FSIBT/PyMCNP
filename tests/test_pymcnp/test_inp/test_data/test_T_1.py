import pymcnp
from .... import consts
from .... import classes


class Test_T_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.T_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'options': [consts.string.inp.data.t_1.CBEG]},
            {'suffix': 1, 'options': [consts.ast.inp.data.t_1.CBEG]},
            {'suffix': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.t_1.CBEG]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.string.inp.data.t_1.CBEG]}, {'suffix': consts.string.type.INTEGER, 'options': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.T_1
        EXAMPLES_VALID = [consts.string.inp.data.T_1]
        EXAMPLES_INVALID = ['hello']
