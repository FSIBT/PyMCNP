import pymcnp
from ..... import consts
from ..... import classes


class Test_Background:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Background
        EXAMPLES_VALID = [{'number': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Background
        EXAMPLES_VALID = [consts.string.inp.data.embed.BACKGROUND]
        EXAMPLES_INVALID = ['hello']


class Test_BackgroundBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.embed.BackgroundBuilder
        EXAMPLES_VALID = [{'number': consts.string.type.INTEGER}, {'number': 1}, {'number': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]
