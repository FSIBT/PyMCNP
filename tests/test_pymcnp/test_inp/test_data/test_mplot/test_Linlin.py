import pymcnp
from ..... import consts
from ..... import classes


class Test_Linlin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Linlin
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Linlin
        EXAMPLES_VALID = [consts.string.inp.data.mplot.LINLIN]
        EXAMPLES_INVALID = ['hello']


class Test_LinlinBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.LinlinBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
