import pymcnp
from ..... import consts
from ..... import classes


class Test_Cop:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Cop
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Cop
        EXAMPLES_VALID = [consts.string.inp.data.mplot.COP]
        EXAMPLES_INVALID = ['hello']


class Test_CopBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.CopBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
