import pymcnp
from ...... import consts
from ...... import classes


class Test_All:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.contour.All
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.contour.All
        EXAMPLES_VALID = [consts.string.inp.data.mplot.contour.ALL]
        EXAMPLES_INVALID = ['hello']


class Test_AllBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.contour.AllBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
