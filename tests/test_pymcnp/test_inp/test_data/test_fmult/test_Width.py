import pymcnp
from ..... import consts
from ..... import classes


class Test_Width:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmult.Width
        EXAMPLES_VALID = [{'width': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'width': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmult.Width
        EXAMPLES_VALID = [consts.string.inp.data.fmult.WIDTH]
        EXAMPLES_INVALID = ['hello']


class Test_WidthBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmult.WidthBuilder
        EXAMPLES_VALID = [{'width': consts.string.type.REAL}, {'width': 3.1}, {'width': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'width': None}]
