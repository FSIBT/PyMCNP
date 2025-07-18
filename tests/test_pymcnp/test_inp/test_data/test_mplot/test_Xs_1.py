import pymcnp
from ..... import consts
from ..... import classes


class Test_Xs_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Xs_1
        EXAMPLES_VALID = [{'m': consts.string.types.ZAID}, {'m': consts.ast.types.ZAID}]
        EXAMPLES_INVALID = [{'m': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Xs_1
        EXAMPLES_VALID = [consts.string.inp.data.mplot.XS_1]
        EXAMPLES_INVALID = ['hello']
