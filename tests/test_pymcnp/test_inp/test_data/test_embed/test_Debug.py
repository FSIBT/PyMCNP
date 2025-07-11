import pymcnp
from ..... import consts
from ..... import classes


class Test_Debug:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Debug
        EXAMPLES_VALID = [{'parameter': 'echomesh'}, {'parameter': pymcnp.types.String('echomesh')}]
        EXAMPLES_INVALID = [{'parameter': None}, {'parameter': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Debug
        EXAMPLES_VALID = [consts.string.inp.data.embed.DEBUG]
        EXAMPLES_INVALID = ['hello']
