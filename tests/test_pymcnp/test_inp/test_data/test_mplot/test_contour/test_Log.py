import pymcnp
from ...... import consts
from ...... import classes


class Test_Log:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.contour.Log
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.contour.Log
        EXAMPLES_VALID = [consts.string.inp.data.mplot.contour.LOG]
        EXAMPLES_INVALID = ['hello']


class Test_LogBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.contour.LogBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
