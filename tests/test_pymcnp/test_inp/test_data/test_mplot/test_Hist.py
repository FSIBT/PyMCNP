import pymcnp
from ..... import consts
from ..... import classes


class Test_Hist:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Hist
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Hist
        EXAMPLES_VALID = [consts.string.inp.data.mplot.HIST]
        EXAMPLES_INVALID = ['hello']


class Test_HistBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.HistBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
