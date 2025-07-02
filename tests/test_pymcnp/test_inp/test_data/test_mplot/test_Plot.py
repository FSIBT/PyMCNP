import pymcnp
from ..... import consts
from ..... import classes


class Test_Plot:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Plot
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Plot
        EXAMPLES_VALID = [consts.string.inp.data.mplot.PLOT]
        EXAMPLES_INVALID = ['hello']


class Test_PlotBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.PlotBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
