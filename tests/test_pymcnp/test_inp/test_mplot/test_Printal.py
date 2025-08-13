import pymcnp
from .... import consts
from .... import classes


class Test_Printal:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Printal
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Printal
        EXAMPLES_VALID = [consts.string.inp.mplot.PRINTAL]
        EXAMPLES_INVALID = ['hello']
