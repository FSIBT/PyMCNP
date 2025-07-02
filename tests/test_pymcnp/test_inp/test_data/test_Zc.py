import pymcnp
from .... import consts
from .... import classes


class Test_Zc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Zc
        EXAMPLES_VALID = [{'anything': consts.ast.type.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Zc
        EXAMPLES_VALID = [consts.string.inp.data.ZC]
        EXAMPLES_INVALID = ['hello']


class Test_ZcBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ZcBuilder
        EXAMPLES_VALID = [{'anything': consts.string.type.STRING}, {'anything': consts.ast.type.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []
