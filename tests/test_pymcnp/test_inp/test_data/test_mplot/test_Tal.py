import pymcnp
from ..... import consts
from ..... import classes


class Test_Tal:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Tal
        EXAMPLES_VALID = [{'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Tal
        EXAMPLES_VALID = [consts.string.inp.data.mplot.TAL]
        EXAMPLES_INVALID = ['hello']


class Test_TalBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.TalBuilder
        EXAMPLES_VALID = [{'n': consts.string.type.INTEGER}, {'n': 1}, {'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]
