import pymcnp
from .... import consts
from .... import classes


class Test_Status:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Status
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Status
        EXAMPLES_VALID = [consts.string.inp.mplot.STATUS]
        EXAMPLES_INVALID = ['hello']
