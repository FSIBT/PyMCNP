import pymcnp
from ... import consts
from ... import classes


class Test_Embed:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Embed
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'options': [consts.string.inp.embed.BACKGROUND]},
            {'suffix': 1, 'options': [consts.ast.inp.embed.BACKGROUND]},
            {'suffix': consts.ast.types.INTEGER, 'options': [consts.ast.inp.embed.BACKGROUND]},
            {'suffix': consts.string.types.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.string.inp.embed.BACKGROUND]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Embed
        EXAMPLES_VALID = [consts.string.inp.EMBED]
        EXAMPLES_INVALID = ['hello']
