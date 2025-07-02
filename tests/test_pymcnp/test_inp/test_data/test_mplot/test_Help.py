import pymcnp
from ..... import consts
from ..... import classes


class Test_Help:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Help
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Help
        EXAMPLES_VALID = [consts.string.inp.data.mplot.HELP]
        EXAMPLES_INVALID = ['hello']


class Test_HelpBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.HelpBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
