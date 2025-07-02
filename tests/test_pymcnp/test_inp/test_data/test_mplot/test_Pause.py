import pymcnp
from ..... import consts
from ..... import classes


class Test_Pause:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Pause
        EXAMPLES_VALID = [{'n': consts.ast.type.INTEGER}, {'n': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Pause
        EXAMPLES_VALID = [consts.string.inp.data.mplot.PAUSE]
        EXAMPLES_INVALID = ['hello']


class Test_PauseBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.PauseBuilder
        EXAMPLES_VALID = [{'n': consts.string.type.INTEGER}, {'n': 1}, {'n': consts.ast.type.INTEGER}, {'n': None}]
        EXAMPLES_INVALID = []
