import pymcnp
from .... import consts
from .... import classes


class Test_Hist:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Hist
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Hist
        EXAMPLES_VALID = [consts.string.inp.mplot.HIST]
        EXAMPLES_INVALID = ['hello']
