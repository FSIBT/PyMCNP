import pymcnp
from ..... import consts
from ..... import classes


class Test_Xtitle:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Xtitle
        EXAMPLES_VALID = [{'aa': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'aa': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Xtitle
        EXAMPLES_VALID = [consts.string.inp.data.mplot.XTITLE]
        EXAMPLES_INVALID = ['hello']


class Test_XtitleBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.XtitleBuilder
        EXAMPLES_VALID = [{'aa': consts.string.type.STRING}, {'aa': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'aa': None}]
