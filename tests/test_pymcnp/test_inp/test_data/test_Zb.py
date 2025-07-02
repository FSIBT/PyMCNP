import pymcnp
from .... import consts
from .... import classes


class Test_Zb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Zb
        EXAMPLES_VALID = [{'anything': consts.ast.type.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Zb
        EXAMPLES_VALID = [consts.string.inp.data.ZB]
        EXAMPLES_INVALID = ['hello']


class Test_ZbBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ZbBuilder
        EXAMPLES_VALID = [{'anything': consts.string.type.STRING}, {'anything': consts.ast.type.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []
