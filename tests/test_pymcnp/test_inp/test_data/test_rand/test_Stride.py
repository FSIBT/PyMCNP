import pymcnp
from ..... import consts
from ..... import classes


class Test_Stride:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.rand.Stride
        EXAMPLES_VALID = [{'stride': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'stride': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.rand.Stride
        EXAMPLES_VALID = [consts.string.inp.data.rand.STRIDE]
        EXAMPLES_INVALID = ['hello']


class Test_StrideBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.rand.StrideBuilder
        EXAMPLES_VALID = [{'stride': consts.string.type.INTEGER}, {'stride': 1}, {'stride': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'stride': None}]
