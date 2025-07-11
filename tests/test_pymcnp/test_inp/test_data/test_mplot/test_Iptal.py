import pymcnp
from ..... import consts
from ..... import classes


class Test_Iptal:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Iptal
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Iptal
        EXAMPLES_VALID = [consts.string.inp.data.mplot.IPTAL]
        EXAMPLES_INVALID = ['hello']
