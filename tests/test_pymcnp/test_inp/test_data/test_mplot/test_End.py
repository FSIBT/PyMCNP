import pymcnp
from ..... import consts
from ..... import classes


class Test_End:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.End
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.End
        EXAMPLES_VALID = [consts.string.inp.data.mplot.END]
        EXAMPLES_INVALID = ['hello']


class Test_EndBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.EndBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
