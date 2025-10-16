import pymcnp
from .... import consts
from .... import classes


class Test_Debug:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embed.Debug
        EXAMPLES_VALID = [{'parameter': 'echomesh'}, {'parameter': pymcnp.types.String('echomesh')}]
        EXAMPLES_INVALID = [{'parameter': None}, {'parameter': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embed.Debug
        EXAMPLES_VALID = [consts.string.inp.embed.DEBUG]
        EXAMPLES_INVALID = ['hello']
