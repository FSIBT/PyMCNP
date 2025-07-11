import pymcnp
from ...... import consts
from ...... import classes


class Test_Noall:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.contour.Noall
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.contour.Noall
        EXAMPLES_VALID = [consts.string.inp.data.mplot.contour.NOALL]
        EXAMPLES_INVALID = ['hello']
