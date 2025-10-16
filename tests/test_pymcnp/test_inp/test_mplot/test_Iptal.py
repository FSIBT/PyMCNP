import pymcnp
from .... import consts
from .... import classes


class Test_Iptal:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Iptal
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Iptal
        EXAMPLES_VALID = [consts.string.inp.mplot.IPTAL]
        EXAMPLES_INVALID = ['hello']
