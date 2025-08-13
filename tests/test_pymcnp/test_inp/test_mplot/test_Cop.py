import pymcnp
from .... import consts
from .... import classes


class Test_Cop:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Cop
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Cop
        EXAMPLES_VALID = [consts.string.inp.mplot.COP]
        EXAMPLES_INVALID = ['hello']
