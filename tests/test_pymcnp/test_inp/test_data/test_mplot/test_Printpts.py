import pymcnp
from ..... import consts
from ..... import classes


class Test_Printpts:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Printpts
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Printpts
        EXAMPLES_VALID = [consts.string.inp.data.mplot.PRINTPTS]
        EXAMPLES_INVALID = ['hello']
