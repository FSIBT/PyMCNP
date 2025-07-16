import pymcnp
from ..... import consts
from ..... import classes


class Test_Meein:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Meein
        EXAMPLES_VALID = [{'filename': consts.string.types.STRING}, {'filename': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Meein
        EXAMPLES_VALID = [consts.string.inp.data.embed.MEEIN]
        EXAMPLES_INVALID = ['hello']
