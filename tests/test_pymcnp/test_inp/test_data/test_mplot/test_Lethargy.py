import pymcnp
from ..... import consts
from ..... import classes


class Test_Lethargy:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Lethargy
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Lethargy
        EXAMPLES_VALID = [consts.string.inp.data.mplot.LETHARGY]
        EXAMPLES_INVALID = ['hello']
