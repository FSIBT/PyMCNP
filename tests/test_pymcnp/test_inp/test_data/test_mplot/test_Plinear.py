import pymcnp
from ..... import consts
from ..... import classes


class Test_Plinear:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Plinear
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Plinear
        EXAMPLES_VALID = [consts.string.inp.data.mplot.PLINEAR]
        EXAMPLES_INVALID = ['hello']
