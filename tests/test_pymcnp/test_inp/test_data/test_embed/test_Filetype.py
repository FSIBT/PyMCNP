import pymcnp
from ..... import consts
from ..... import classes


class Test_Filetype:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Filetype
        EXAMPLES_VALID = [{'kind': 'ascii'}, {'kind': pymcnp.types.String('ascii')}]
        EXAMPLES_INVALID = [{'kind': None}, {'kind': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Filetype
        EXAMPLES_VALID = [consts.string.inp.data.embed.FILETYPE]
        EXAMPLES_INVALID = ['hello']
