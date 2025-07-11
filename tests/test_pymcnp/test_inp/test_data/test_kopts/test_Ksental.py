import pymcnp
from ..... import consts
from ..... import classes


class Test_Ksental:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kopts.Ksental
        EXAMPLES_VALID = [{'fileopt': 'mctal'}, {'fileopt': pymcnp.types.String('mctal')}]
        EXAMPLES_INVALID = [{'fileopt': None}, {'fileopt': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kopts.Ksental
        EXAMPLES_VALID = [consts.string.inp.data.kopts.KSENTAL]
        EXAMPLES_INVALID = ['hello']
