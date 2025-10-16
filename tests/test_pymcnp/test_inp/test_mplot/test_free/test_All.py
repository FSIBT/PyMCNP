import pymcnp
from ..... import consts
from ..... import classes


class Test_All:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.free.All
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.free.All
        EXAMPLES_VALID = [consts.string.inp.mplot.free.ALL]
        EXAMPLES_INVALID = ['hello']
