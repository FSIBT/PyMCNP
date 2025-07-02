import pymcnp
from ...... import consts
from ...... import classes


class Test_Color:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.contour.Color
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.contour.Color
        EXAMPLES_VALID = [consts.string.inp.data.mplot.contour.COLOR]
        EXAMPLES_INVALID = ['hello']


class Test_ColorBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.contour.ColorBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
