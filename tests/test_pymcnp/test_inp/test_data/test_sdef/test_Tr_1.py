import pymcnp
from ..... import consts
from ..... import classes


class Test_Tr_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Tr_1
        EXAMPLES_VALID = [{'number': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Tr_1
        EXAMPLES_VALID = [consts.string.inp.data.sdef.TR_1]
        EXAMPLES_INVALID = ['hello']


class Test_TrBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.TrBuilder_1
        EXAMPLES_VALID = [{'number': consts.string.type.INTEGER}, {'number': 1}, {'number': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]
