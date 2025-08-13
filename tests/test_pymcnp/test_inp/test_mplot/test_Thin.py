import pymcnp
from .... import consts
from .... import classes


class Test_Thin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Thin
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Thin
        EXAMPLES_VALID = [consts.string.inp.mplot.THIN]
        EXAMPLES_INVALID = ['hello']
