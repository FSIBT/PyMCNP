import pymcnp
from ..... import consts
from ..... import classes


class Test_Tbin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Tbin
        EXAMPLES_VALID = [{'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Tbin
        EXAMPLES_VALID = [consts.string.inp.data.mplot.TBIN]
        EXAMPLES_INVALID = ['hello']


class Test_TbinBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.TbinBuilder
        EXAMPLES_VALID = [{'n': consts.string.type.INTEGER}, {'n': 1}, {'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]
