import pymcnp
from .... import consts
from .... import classes


class Test_Tally:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Tally
        EXAMPLES_VALID = [{'n': consts.string.types.INTEGER}, {'n': 1}, {'n': consts.ast.types.INTEGER}, {'n': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Tally
        EXAMPLES_VALID = [consts.string.inp.mplot.TALLY]
        EXAMPLES_INVALID = ['hello']
