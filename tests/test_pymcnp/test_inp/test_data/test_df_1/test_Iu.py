import pymcnp
from ..... import consts
from ..... import classes


class Test_Iu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.df_1.Iu
        EXAMPLES_VALID = [{'units': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'units': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.df_1.Iu
        EXAMPLES_VALID = [consts.string.inp.data.df_1.IU]
        EXAMPLES_INVALID = ['hello']


class Test_IuBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.df_1.IuBuilder
        EXAMPLES_VALID = [{'units': consts.string.type.INTEGER}, {'units': 1}, {'units': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'units': None}]
