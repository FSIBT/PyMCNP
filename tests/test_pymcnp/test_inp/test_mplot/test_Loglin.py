import pymcnp
from .... import consts
from .... import classes


class Test_Loglin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Loglin
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Loglin
        EXAMPLES_VALID = [consts.string.inp.mplot.LOGLIN]
        EXAMPLES_INVALID = ['hello']
