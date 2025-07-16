import pymcnp
from ..... import consts
from ..... import classes


class Test_Meeout:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Meeout
        EXAMPLES_VALID = [{'filename': consts.string.types.STRING}, {'filename': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Meeout
        EXAMPLES_VALID = [consts.string.inp.data.embed.MEEOUT]
        EXAMPLES_INVALID = ['hello']
