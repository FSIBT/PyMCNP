import pymcnp
from ...... import consts
from ...... import classes


class Test_Nocolor:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.contour.Nocolor
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.contour.Nocolor
        EXAMPLES_VALID = [consts.string.inp.data.mplot.contour.NOCOLOR]
        EXAMPLES_INVALID = ['hello']
