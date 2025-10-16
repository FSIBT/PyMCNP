import pymcnp
from .... import consts
from .... import classes


class Test_Help:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Help
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Help
        EXAMPLES_VALID = [consts.string.inp.mplot.HELP]
        EXAMPLES_INVALID = ['hello']
