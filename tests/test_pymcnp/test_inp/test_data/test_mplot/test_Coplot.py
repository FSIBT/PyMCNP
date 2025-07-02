import pymcnp
from ..... import consts
from ..... import classes


class Test_Coplot:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Coplot
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Coplot
        EXAMPLES_VALID = [consts.string.inp.data.mplot.COPLOT]
        EXAMPLES_INVALID = ['hello']


class Test_CoplotBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.CoplotBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
