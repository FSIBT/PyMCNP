import pymcnp
from ..... import consts
from ..... import classes


class Test_Wmctal:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Wmctal
        EXAMPLES_VALID = [{'filename': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Wmctal
        EXAMPLES_VALID = [consts.string.inp.data.mplot.WMCTAL]
        EXAMPLES_INVALID = ['hello']


class Test_WmctalBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.WmctalBuilder
        EXAMPLES_VALID = [{'filename': consts.string.type.STRING}, {'filename': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]
