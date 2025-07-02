import pymcnp
from .... import consts
from .... import classes


class Test_Df_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Df_1
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.df_1.FAC]}]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.ast.inp.data.df_1.FAC]}, {'suffix': consts.ast.type.INTEGER, 'options': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Df_1
        EXAMPLES_VALID = [consts.string.inp.data.DF_1]
        EXAMPLES_INVALID = ['hello']


class Test_DfBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.DfBuilder_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'options': [consts.string.inp.data.df_1.FAC]},
            {'suffix': 1, 'options': [consts.builder.inp.data.df_1.FAC]},
            {'suffix': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.df_1.FAC]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.string.inp.data.df_1.FAC]}, {'suffix': consts.string.type.INTEGER, 'options': None}]
