import pymcnp
from ..... import consts
from ..... import classes


class Test_Noerrbar:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Noerrbar
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Noerrbar
        EXAMPLES_VALID = [consts.string.inp.data.mplot.NOERRBAR]
        EXAMPLES_INVALID = ['hello']


class Test_NoerrbarBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.NoerrbarBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
