import pymcnp
from ..... import consts
from ..... import classes


class Test_Rmctal:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Rmctal
        EXAMPLES_VALID = [{'filename': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Rmctal
        EXAMPLES_VALID = [consts.string.inp.data.mplot.RMCTAL]
        EXAMPLES_INVALID = ['hello']


class Test_RmctalBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.RmctalBuilder
        EXAMPLES_VALID = [{'filename': consts.string.type.STRING}, {'filename': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]
