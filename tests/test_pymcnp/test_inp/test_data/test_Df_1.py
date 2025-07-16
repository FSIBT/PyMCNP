import pymcnp
from .... import consts
from .... import classes


class Test_Df_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Df_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'options': [consts.string.inp.data.df_1.FAC]},
            {'suffix': 1, 'options': [consts.ast.inp.data.df_1.FAC]},
            {'suffix': consts.ast.types.INTEGER, 'options': [consts.ast.inp.data.df_1.FAC]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.string.inp.data.df_1.FAC]}, {'suffix': consts.string.types.INTEGER, 'options': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Df_1
        EXAMPLES_VALID = [consts.string.inp.data.DF_1]
        EXAMPLES_INVALID = ['hello']
