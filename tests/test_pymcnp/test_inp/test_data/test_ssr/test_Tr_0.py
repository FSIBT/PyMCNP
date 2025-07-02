import pymcnp
from ..... import consts
from ..... import classes


class Test_Tr_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Tr_0
        EXAMPLES_VALID = [{'number': consts.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Tr_0
        EXAMPLES_VALID = [consts.string.inp.data.ssr.TR_0]
        EXAMPLES_INVALID = ['hello']


class Test_TrBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssr.TrBuilder_0
        EXAMPLES_VALID = [{'number': consts.string.type.DISTRIBUTIONNUMBER}, {'number': consts.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'number': None}]
