import pymcnp
from ..... import consts
from ..... import classes


class Test_Nreact:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.tropt.Nreact
        EXAMPLES_VALID = [{'setting': 'off'}, {'setting': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.tropt.Nreact
        EXAMPLES_VALID = [consts.string.inp.data.tropt.NREACT]
        EXAMPLES_INVALID = ['hello']
