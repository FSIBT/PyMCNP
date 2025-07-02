import pymcnp
from ..... import consts
from ..... import classes


class Test_Fmesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Fmesh
        EXAMPLES_VALID = [{'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Fmesh
        EXAMPLES_VALID = [consts.string.inp.data.mplot.FMESH]
        EXAMPLES_INVALID = ['hello']


class Test_FmeshBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.FmeshBuilder
        EXAMPLES_VALID = [{'n': consts.string.type.INTEGER}, {'n': 1}, {'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]
