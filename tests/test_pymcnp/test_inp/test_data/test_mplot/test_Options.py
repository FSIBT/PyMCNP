import pymcnp
from ..... import consts
from ..... import classes


class Test_Options:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Options
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Options
        EXAMPLES_VALID = [consts.string.inp.data.mplot.OPTIONS]
        EXAMPLES_INVALID = ['hello']


class Test_OptionsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.OptionsBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
