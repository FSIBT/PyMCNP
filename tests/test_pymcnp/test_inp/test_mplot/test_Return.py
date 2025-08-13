import pymcnp
from .... import consts
from .... import classes


class Test_Return:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Return
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Return
        EXAMPLES_VALID = [consts.string.inp.mplot.RETURN]
        EXAMPLES_INVALID = ['hello']
