import pymcnp
from .... import consts
from .... import classes


class Test_Length:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embed.Length
        EXAMPLES_VALID = [{'factor': consts.string.types.REAL}, {'factor': 3.1}, {'factor': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embed.Length
        EXAMPLES_VALID = [consts.string.inp.embed.LENGTH]
        EXAMPLES_INVALID = ['hello']
