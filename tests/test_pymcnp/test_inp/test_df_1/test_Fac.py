import pymcnp
from .... import consts
from .... import classes


class Test_Fac:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.df_1.Fac
        EXAMPLES_VALID = [{'normalization': consts.string.types.INTEGER}, {'normalization': 1}, {'normalization': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'normalization': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.df_1.Fac
        EXAMPLES_VALID = [consts.string.inp.df_1.FAC]
        EXAMPLES_INVALID = ['hello']
