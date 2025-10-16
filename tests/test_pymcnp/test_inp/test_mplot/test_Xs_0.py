import pymcnp
from .... import consts
from .... import classes


class Test_Xs_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Xs_0
        EXAMPLES_VALID = [{'m': consts.string.types.INTEGER}, {'m': 1}, {'m': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'m': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Xs_0
        EXAMPLES_VALID = [consts.string.inp.mplot.XS_0]
        EXAMPLES_INVALID = ['hello']
