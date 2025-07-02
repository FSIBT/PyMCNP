import pymcnp
from ..... import consts
from ..... import classes


class Test_Linlog:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Linlog
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Linlog
        EXAMPLES_VALID = [consts.string.inp.data.mplot.LINLOG]
        EXAMPLES_INVALID = ['hello']


class Test_LinlogBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.LinlogBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
