import pymcnp
from ...... import consts
from ...... import classes


class Test_All:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.free.All
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.free.All
        EXAMPLES_VALID = [consts.string.inp.data.mplot.free.ALL]
        EXAMPLES_INVALID = ['hello']


class Test_AllBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.free.AllBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
