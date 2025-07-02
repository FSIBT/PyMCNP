import pymcnp
from ..... import consts
from ..... import classes


class Test_Meeout:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Meeout
        EXAMPLES_VALID = [{'filename': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Meeout
        EXAMPLES_VALID = [consts.string.inp.data.embed.MEEOUT]
        EXAMPLES_INVALID = ['hello']


class Test_MeeoutBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.embed.MeeoutBuilder
        EXAMPLES_VALID = [{'filename': consts.string.type.STRING}, {'filename': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]
