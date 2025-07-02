import pymcnp
from .... import consts
from .... import classes


class Test_Embed:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Embed
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.embed.BACKGROUND]}, {'suffix': consts.ast.type.INTEGER, 'options': None}]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.ast.inp.data.embed.BACKGROUND]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Embed
        EXAMPLES_VALID = [consts.string.inp.data.EMBED]
        EXAMPLES_INVALID = ['hello']


class Test_EmbedBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.EmbedBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'options': [consts.string.inp.data.embed.BACKGROUND]},
            {'suffix': 1, 'options': [consts.builder.inp.data.embed.BACKGROUND]},
            {'suffix': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.embed.BACKGROUND]},
            {'suffix': consts.string.type.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.string.inp.data.embed.BACKGROUND]}]
