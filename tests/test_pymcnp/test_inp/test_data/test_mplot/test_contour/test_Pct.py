import pymcnp
from ...... import consts
from ...... import classes


class Test_Pct:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.contour.Pct
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.contour.Pct
        EXAMPLES_VALID = [consts.string.inp.data.mplot.contour.PCT]
        EXAMPLES_INVALID = ['hello']


class Test_PctBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.contour.PctBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
