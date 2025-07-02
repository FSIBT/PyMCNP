import pymcnp
from ..... import consts
from ..... import classes


class Test_Mat:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.pert.Mat
        EXAMPLES_VALID = [{'material': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'material': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.pert.Mat
        EXAMPLES_VALID = [consts.string.inp.data.pert.MAT]
        EXAMPLES_INVALID = ['hello']


class Test_MatBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.pert.MatBuilder
        EXAMPLES_VALID = [{'material': consts.string.type.INTEGER}, {'material': 1}, {'material': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'material': None}]
