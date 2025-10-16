import pymcnp
from .... import consts
from .... import classes


class Test_Coplot:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Coplot
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Coplot
        EXAMPLES_VALID = [consts.string.inp.mplot.COPLOT]
        EXAMPLES_INVALID = ['hello']
