import pymcnp
from .... import consts
from .... import classes


class Test_Ksental:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kopts.Ksental
        EXAMPLES_VALID = [{'fileopt': 'mctal'}, {'fileopt': pymcnp.types.String('mctal')}]
        EXAMPLES_INVALID = [{'fileopt': None}, {'fileopt': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kopts.Ksental
        EXAMPLES_VALID = [consts.string.inp.kopts.KSENTAL]
        EXAMPLES_INVALID = ['hello']
