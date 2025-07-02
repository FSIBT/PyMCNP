import pymcnp
from ..... import consts
from ..... import classes


class Test_Fac:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.df_1.Fac
        EXAMPLES_VALID = [{'normalization': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'normalization': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.df_1.Fac
        EXAMPLES_VALID = [consts.string.inp.data.df_1.FAC]
        EXAMPLES_INVALID = ['hello']


class Test_FacBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.df_1.FacBuilder
        EXAMPLES_VALID = [{'normalization': consts.string.type.INTEGER}, {'normalization': 1}, {'normalization': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'normalization': None}]
