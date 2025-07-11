import pymcnp
from ..... import consts
from ..... import classes


class Test_Fmatreduce:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kopts.Fmatreduce
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kopts.Fmatreduce
        EXAMPLES_VALID = [consts.string.inp.data.kopts.FMATREDUCE]
        EXAMPLES_INVALID = ['hello']
