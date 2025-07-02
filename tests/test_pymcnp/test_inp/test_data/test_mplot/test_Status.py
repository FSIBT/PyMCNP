import pymcnp
from ..... import consts
from ..... import classes


class Test_Status:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Status
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Status
        EXAMPLES_VALID = [consts.string.inp.data.mplot.STATUS]
        EXAMPLES_INVALID = ['hello']


class Test_StatusBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.StatusBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
