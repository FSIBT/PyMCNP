import pymcnp
from .... import consts
from .... import classes


class Test_Embed:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embee.Embed
        EXAMPLES_VALID = [{'number': consts.string.types.INTEGER}, {'number': 1}, {'number': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embee.Embed
        EXAMPLES_VALID = [consts.string.inp.embee.EMBED]
        EXAMPLES_INVALID = ['hello']
