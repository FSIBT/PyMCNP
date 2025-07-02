import pymcnp
from .... import consts
from .... import classes


class Test_Za:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Za
        EXAMPLES_VALID = [{'anything': consts.ast.type.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Za
        EXAMPLES_VALID = [consts.string.inp.data.ZA]
        EXAMPLES_INVALID = ['hello']


class Test_ZaBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ZaBuilder
        EXAMPLES_VALID = [{'anything': consts.string.type.STRING}, {'anything': consts.ast.type.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []
