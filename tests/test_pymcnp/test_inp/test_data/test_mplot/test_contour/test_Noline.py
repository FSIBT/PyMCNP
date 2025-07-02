import pymcnp
from ...... import consts
from ...... import classes


class Test_Noline:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.contour.Noline
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.contour.Noline
        EXAMPLES_VALID = [consts.string.inp.data.mplot.contour.NOLINE]
        EXAMPLES_INVALID = ['hello']


class Test_NolineBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.contour.NolineBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
