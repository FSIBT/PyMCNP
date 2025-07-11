import pymcnp
from ..... import consts
from ..... import classes


class Test_Calcvols:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Calcvols
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Calcvols
        EXAMPLES_VALID = [consts.string.inp.data.embed.CALCVOLS]
        EXAMPLES_INVALID = ['hello']
