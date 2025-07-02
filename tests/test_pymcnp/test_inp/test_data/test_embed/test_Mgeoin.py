import pymcnp
from ..... import consts
from ..... import classes


class Test_Mgeoin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Mgeoin
        EXAMPLES_VALID = [{'filename': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Mgeoin
        EXAMPLES_VALID = [consts.string.inp.data.embed.MGEOIN]
        EXAMPLES_INVALID = ['hello']


class Test_MgeoinBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.embed.MgeoinBuilder
        EXAMPLES_VALID = [{'filename': consts.string.type.STRING}, {'filename': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]
