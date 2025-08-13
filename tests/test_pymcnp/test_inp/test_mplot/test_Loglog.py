import pymcnp
from .... import consts
from .... import classes


class Test_Loglog:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Loglog
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Loglog
        EXAMPLES_VALID = [consts.string.inp.mplot.LOGLOG]
        EXAMPLES_INVALID = ['hello']
