import pymcnp
from .... import consts
from .... import classes


class Test_Below:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Below
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Below
        EXAMPLES_VALID = [consts.string.inp.mplot.BELOW]
        EXAMPLES_INVALID = ['hello']
