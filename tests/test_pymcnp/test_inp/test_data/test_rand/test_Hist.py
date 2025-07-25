import pymcnp
from ..... import consts
from ..... import classes


class Test_Hist:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.rand.Hist
        EXAMPLES_VALID = [{'hist': consts.string.types.INTEGER}, {'hist': 1}, {'hist': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'hist': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.rand.Hist
        EXAMPLES_VALID = [consts.string.inp.data.rand.HIST]
        EXAMPLES_INVALID = ['hello']
