import pymcnp
from ..... import consts
from ..... import classes


class Test_Thin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Thin
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Thin
        EXAMPLES_VALID = [consts.string.inp.data.mplot.THIN]
        EXAMPLES_INVALID = ['hello']


class Test_ThinBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.ThinBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
