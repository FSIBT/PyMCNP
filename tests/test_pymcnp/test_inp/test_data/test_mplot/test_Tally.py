import pymcnp
from ..... import consts
from ..... import classes


class Test_Tally:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Tally
        EXAMPLES_VALID = [{'n': consts.string.type.INTEGER}, {'n': 1}, {'n': consts.ast.type.INTEGER}, {'n': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Tally
        EXAMPLES_VALID = [consts.string.inp.data.mplot.TALLY]
        EXAMPLES_INVALID = ['hello']
