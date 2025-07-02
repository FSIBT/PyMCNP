import pymcnp
from ..... import consts
from ..... import classes


class Test_Coni:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.t_1.Coni
        EXAMPLES_VALID = [{'time': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.t_1.Coni
        EXAMPLES_VALID = [consts.string.inp.data.t_1.CONI]
        EXAMPLES_INVALID = ['hello']


class Test_ConiBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.t_1.ConiBuilder
        EXAMPLES_VALID = [{'time': consts.string.type.REAL}, {'time': 3.1}, {'time': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'time': None}]
