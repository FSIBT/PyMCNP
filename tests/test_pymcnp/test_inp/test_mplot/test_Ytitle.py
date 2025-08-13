import pymcnp
from .... import consts
from .... import classes


class Test_Ytitle:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Ytitle
        EXAMPLES_VALID = [{'aa': consts.string.types.STRING}, {'aa': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'aa': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Ytitle
        EXAMPLES_VALID = [consts.string.inp.mplot.YTITLE]
        EXAMPLES_INVALID = ['hello']
