import pymcnp
from .... import consts
from .... import classes


class Test_Bar:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Bar
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Bar
        EXAMPLES_VALID = [consts.string.inp.mplot.BAR]
        EXAMPLES_INVALID = ['hello']
