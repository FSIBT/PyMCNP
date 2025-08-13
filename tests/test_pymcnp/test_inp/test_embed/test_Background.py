import pymcnp
from .... import consts
from .... import classes


class Test_Background:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embed.Background
        EXAMPLES_VALID = [{'number': consts.string.types.INTEGER}, {'number': 1}, {'number': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embed.Background
        EXAMPLES_VALID = [consts.string.inp.embed.BACKGROUND]
        EXAMPLES_INVALID = ['hello']
