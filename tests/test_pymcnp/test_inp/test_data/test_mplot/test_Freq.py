import pymcnp
from ..... import consts
from ..... import classes


class Test_Freq:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Freq
        EXAMPLES_VALID = [{'n': consts.string.type.INTEGER}, {'n': 1}, {'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Freq
        EXAMPLES_VALID = [consts.string.inp.data.mplot.FREQ]
        EXAMPLES_INVALID = ['hello']
