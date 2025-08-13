import pymcnp
from ..... import consts
from ..... import classes


class Test_Lin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.contour.Lin
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.contour.Lin
        EXAMPLES_VALID = [consts.string.inp.mplot.contour.LIN]
        EXAMPLES_INVALID = ['hello']
