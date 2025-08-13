import pymcnp
from .... import consts
from .... import classes


class Test_Printpts:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Printpts
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Printpts
        EXAMPLES_VALID = [consts.string.inp.mplot.PRINTPTS]
        EXAMPLES_INVALID = ['hello']
