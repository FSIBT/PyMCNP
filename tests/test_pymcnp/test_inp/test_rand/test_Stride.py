import pymcnp
from .... import consts
from .... import classes


class Test_Stride:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.rand.Stride
        EXAMPLES_VALID = [{'stride': consts.string.types.INTEGER}, {'stride': 1}, {'stride': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'stride': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.rand.Stride
        EXAMPLES_VALID = [consts.string.inp.rand.STRIDE]
        EXAMPLES_INVALID = ['hello']
