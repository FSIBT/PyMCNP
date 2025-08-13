import pymcnp
from .... import consts
from .... import classes


class Test_Iu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.df_1.Iu
        EXAMPLES_VALID = [{'units': consts.string.types.INTEGER}, {'units': 1}, {'units': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'units': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.df_1.Iu
        EXAMPLES_VALID = [consts.string.inp.df_1.IU]
        EXAMPLES_INVALID = ['hello']
