import pymcnp
from .... import consts
from .... import classes


class Test_Options:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Options
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Options
        EXAMPLES_VALID = [consts.string.inp.mplot.OPTIONS]
        EXAMPLES_INVALID = ['hello']
