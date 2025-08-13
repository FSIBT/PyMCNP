import pymcnp
from .... import consts
from .... import classes


class Test_Ztitle:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Ztitle
        EXAMPLES_VALID = [{'aa': consts.string.types.STRING}, {'aa': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'aa': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Ztitle
        EXAMPLES_VALID = [consts.string.inp.mplot.ZTITLE]
        EXAMPLES_INVALID = ['hello']
