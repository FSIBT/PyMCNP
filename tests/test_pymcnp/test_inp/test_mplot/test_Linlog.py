import pymcnp
from .... import consts
from .... import classes


class Test_Linlog:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Linlog
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Linlog
        EXAMPLES_VALID = [consts.string.inp.mplot.LINLOG]
        EXAMPLES_INVALID = ['hello']
